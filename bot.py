from bot_root import bot, sessionManager
from auth import *


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
