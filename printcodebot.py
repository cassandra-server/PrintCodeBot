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
usernames_raw = ""

for i in range (1, len(arguments)):
	if (arguments [i] == "-u"):
		usernames_raw = arguments[i+1]
	if (arguments [i] == "-f"):
		code += arguments[i+1] + " "

code += "> .stuff.txt"

usernames = usernames_raw.split(',')
f = open('config/users.txt', 'r')
lines = []
for line in f:
	lines.append(line)
f.close()

usernames_def = []

for username in usernames:
	if username.isnumeric():
		usernames_def.append(username)
	else:
		for line in lines:
			if username == line.split(' ')[0]:
				usernames_def.append(line.split(' ')[1])
				break

subprocess.call(code, shell=True)

f = open(".stuff.txt", 'r')
text2 = ""

for line in f:
    text2 += line

f.close()

for USERNAME in usernames_def:
	bot.send_message(chat_id=USERNAME, text=text2)

