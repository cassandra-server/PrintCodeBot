import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import subprocess
import sys


f = open('config/token.txt', 'r')
TOKEN = f.read().replace('\n', '')
f.close()

#updater=Updater(token=TOKEN, use_context=True)
#dispatcher = updater.dispatcher
bot = telegram.Bot(TOKEN)

#updater.start_polling()

arguments = sys.argv
arguments_def = ""

for i in range (1, len(arguments)):
  arguments_def += arguments[i] + " "

arguments_def += "> .stuff.txt"

subprocess.call(arguments_def, shell=True)

f = open(".stuff.txt", 'r')
text2 = ""

for line in f:
    text2 += line

f.close()

bot.send_message(chat_id=CHAT_ID, text=text2)
