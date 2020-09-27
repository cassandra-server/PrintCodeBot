import telegram
import subprocess
import sys

bot = telegram.Bot(TOKEN)

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


bot.send_message(chat_id=USER_ID, text=text2)
