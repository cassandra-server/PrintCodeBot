import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import subprocess
import sys


f = open('config/token.txt', 'r')
TOKEN = f.read().replace('\n', '')
f.close()

bot = telegram.Bot(TOKEN)

arguments = sys.argv
code = ""
USERNAME = ""

for i in range (1, len(arguments)):
	if (arguments [i] == "-u"):
		USERNAME = arguments[i+1]
	if (arguments [i] == "-f"):
		code += arguments[i+1] + " "

code += "> .stuff.txt"

subprocess.call(code, shell=True)

f = open(".stuff.txt", 'r')
text2 = ""

for line in f:
    text2 += line

f.close()

bot.send_message(chat_id=USERNAME, text=text2)
