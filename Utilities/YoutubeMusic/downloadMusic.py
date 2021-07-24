from telegram.ext import Dispatcher, CommandHandler, CallbackQueryHandler
from telegram import BotCommand, InputMediaAudio, BotCommand
import pafy
import os
import re

def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"
    new_title = re.sub(rstr, "", title)  
    return new_title

def music(update,context):
    if len(context.args) == 1:
        url = str(context.args[0])
        if 'youtube.com' in url or 'youtu.be' in url:
            chatid = update.effective_chat.id
            video = pafy.new(url)
            info = str(video).split('\n')
            title = info[0].split(':')[1]
            author = info[1].split(':')[1]
            bestaudio = video.getbestaudio(preftype="m4a")
            music_size = bestaudio.get_filesize()
            audio = f'{bestaudio.title}'
            audiofile = f'/tmp/{validateTitle(audio)}.{bestaudio.extension}'
            if music_size < 1000*1000*10:
                displayImage = "https://i.pcmag.com/imagery/articles/04oP7J3OIykTchX4vhU57vn-28..1569485834.jpg"
                bestaudio.download(audiofile)
                msg = update.message.reply_photo(displayImage,f"downloading... Your audio's size is {music_size/100}KB\n\n🎵 Music: {title} by 🎶 {author}")
                msg.edit_media(InputMediaAudio(open(audiofile,'rb')))
                msg == context.bot.send_message(chatid,f"{str(video)}")
                os.remove(audiofile)
            else: 
                update.message.reply_text("Sorry this file is too big!")
        else:
            update.message.reply_text("Youtube Video Link Please!")
    else:
        update.message.reply_text("Put a link! /music [Youtube video link]")

def add_handler(dp:Dispatcher):
    dp.add_handler(CommandHandler('music', music))

def get_command():
    return [BotCommand('music','Enjoy music from a YouTube video on Telegram!')]



            