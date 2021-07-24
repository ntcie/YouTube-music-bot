from telegram.ext import Dispatcher,CommandHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters, Updater
from telegram import BotCommand
from Utilities import mysystemd
from Utilities.YoutubeMusic import downloadMusic
import os

def read_file_as_str(file_path): 
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")
    all_the_text = open(file_path).read()
    return all_the_text
 
def start(update,context):
    update.message.reply_text("""
Hello! This is the SSwift Bot. 
    """)

TOKEN = read_file_as_str('TOKEN')
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)
downloadMusic.add_handler(dispatcher)

commands = downloadMusic.get_command()
bot = updater.bot
bot.set_my_commands(commands)

updater.start_polling()
print('Started')
mysystemd.ready()

updater.idle()
print('Stopping...')
print('Stopped.')