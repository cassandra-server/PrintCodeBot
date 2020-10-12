import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import subprocess
import sys


def get_data (raw, value): #value: 0 --> default / 1 --> usernames / 2 --> groups
	ug_data = raw.split(',')
	if value == 0:
		path = 'config/defaults.txt'
	elif value == 1:
		path = 'config/users.txt'
	elif value == 2:
		path = 'config/groups.txt'
	f = open(path, 'r')
	lines = []
	for line in f:
		lines.append(line)
	f.close()
	addressees = []
	if value == 2 or value == 0:
		for group in ug_data:
			for line in lines:
				if (group == line.split(' ')[0]):
					if (group == 'token'):
						return line.split(' ')[1].replace('\n','')
					addressees.extend(get_data(line.split(' ')[1].replace('\n',''), 1))
					break
	elif value == 1:
		for username in ug_data:
			if username.isnumeric():
				addressees.append(username)
			else:
				for line in lines:
					if username == line.split(' ')[0]:
						addressees.append(line.split(' ')[1])
						break
	return addressees


def new_configuration ():
	print ("WELCOME TO THE CONFIGURATION OF PRINT CODE BOT")
	print ("----------------------------------------------")
	print ("\nTOKEN:")
	token = input("Paste here your token: ")
	print ("\nUSERNAMES:")
	answer = 'y'
	usernames = []
	while (answer == 'y'):
		usernames.append(input("Write a default username for the machine [alias/id]? "))
		answer = input ("Do you wish to add another username [Y/N]? ").lower()
	f = open ('config/defaults.txt', 'w+')
	f.write ("token " + token + '\n')
	f.write ("addressees ")
	for username in usernames:
		f.write(username + ',')
	f.close()
	print ("CONFIGURATION ENDED! THANKS :)")
	exit()


arguments = sys.argv
if (len(arguments) == 2 and arguments[1] == "-c"):
	new_configuration()

bot = telegram.Bot(str(get_data("token", 0)))

code = ""
usernames_raw = ""
groups_raw = ""
addressees = []
specifiedUsers = False
specifiedGroups = False

for i in range (1, len(arguments)):
	if (arguments [i] == "-u"):
		specifiedUsers = True
		addressees.extend(get_data(arguments[i+1], 1))
	if (arguments [i] == "-g"):
		specifiedGroups = True
		addressees.extend(get_data(arguments[i+1], 2))
	if (arguments [i] == "-f"):
		code += arguments[i+1] + " "


if (specifiedUsers==False and specifiedGroups==False):
	addressees.extend(get_data("addressees", 0))

code += "> .stuff.txt"

subprocess.call(code, shell=True)

f = open(".stuff.txt", 'r')
text2 = ""

for line in f:
    text2 += line

f.close()

for addressee in list(dict.fromkeys(addressees)):
	bot.send_message(chat_id=addressee, text=text2)
