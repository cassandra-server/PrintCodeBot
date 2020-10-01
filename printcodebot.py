import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import subprocess
import sys


def recognize_users (raw, is_group):
	ug_data = raw.split(',')
	if is_group:
		path = 'config/groups.txt'
	else:
		path = 'config/users.txt'
	f = open(path, 'r')
	lines = []
	for line in f:
		lines.append(line)
	f.close()

	addressees = []
	if is_group:
		for group in ug_data:
			for line in lines:
				if group == line.split(' ')[0]:
					addressees.extend(recognize_users(line.split(' ')[1].replace('\n',''), False))
					break
	else:
		for username in ug_data:
			if username.isnumeric():
				addressees.append(username)
			else:
				for line in lines:
					if username == line.split(' ')[0]:
						addressees.append(line.split(' ')[1])
						break
	return addressees


"""
def recognize_users (usernames_raw):
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
	return usernames_def


def recognize_groups (groups_raw):
	groups = groups_raw.split(',')
	f = open ('config/groups.txt', 'r')
	lines = []
	for line in f:
		lines.append(line)
	f.close()

	groups_def = []
	for group in groups:
		for line in lines:
			if group == line.split(' ')[0]:
				groups_def.extend(recognize_users(line.split(' ')[1].replace('\n','')))
				break
	return groups_def
"""

f = open('config/token.txt', 'r')
TOKEN = f.read().replace('\n', '')
f.close()

bot = telegram.Bot(TOKEN)

arguments = sys.argv
code = ""
usernames_raw = ""
groups_raw = ""
addressees = []

for i in range (1, len(arguments)):
	if (arguments [i] == "-u"):
		addressees.extend(recognize_users(arguments[i+1], False))
#		usernames_raw = arguments[i+1]
	if (arguments [i] == "-g"):
#		addressees.extend(recognize_groups(arguments[i+1]))
#		groups_raw = arguments[i+1]
		addressees.extend(recognize_users(arguments[i+1], True))
	if (arguments [i] == "-f"):
		code += arguments[i+1] + " "

code += "> .stuff.txt"

#addressees = recognize_users(usernames_raw)
#groups = recognize_groups(groups_raw)

subprocess.call(code, shell=True)

f = open(".stuff.txt", 'r')
text2 = ""

for line in f:
    text2 += line

f.close()

#for USERNAME in usernames:
#	bot.send_message(chat_id=USERNAME, text=text2)

#for GROUP in groups:
#	print (GROUP)
#	bot.send_message(chat_id=GROUP, text=text2)

for addressee in addressees:
	bot.send_message(chat_id=addressee, text=text2)
