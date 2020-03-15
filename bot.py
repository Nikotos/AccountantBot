#import telebot
#from session import *

from bot_root import bot, sessionManager
from auth import *

#bot = telebot.TeleBot("999326925:AAFveAjhR9MuzKvuKbx4cj9sdF2_SW2h3AY")
#sessionManager = SessionManager()
#
#
#@bot.message_handler(commands=["auth"])
#def auth_func(message):
#    data = message.text.split(" ")
#    if (len(data) == 3):
#        username, pwd = data[1], data[2]
#        sessionID = message.chat.id
#        result = sessionManager.addSession(sessionID, username, pwd)
#        if result:
#            bot.send_message(message.chat.id, "ай малаца")
#        else:
#            bot.send_message(message.chat.id, "пащел нахуй")
#    else:
#        bot.send_message(message.chat.id, "incorrect format")


@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "введитe пароль")

@bot.message_handler(commands=["stop"])
def stop_handler(message):
    sessionID = message.chat.id
    sessionManager.removeSession(sessionID)

@bot.message_handler(commands=["nudes"])
def nudes(message):
    if (sessionManager.isAuthorized(message.chat.id)):
        bot.send_message(message.chat.id, "0-0")
    else:
        bot.send_message(message.chat.id, "не авторизирован")


@bot.message_handler(commands=["dudes"], func=lambda message: sessionManager.isAuthorized(message.chat.id))
def dudes(message):
    bot.send_message(message.chat.id, "0_0")



bot.polling()
