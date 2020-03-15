from bot_root import bot, sessionManager
from session import *


@bot.message_handler(commands=["auth"])
def auth_func(message):
    data = message.text.split(" ")
    if (len(data) == 3):
        username, pwd = data[1], data[2]
        sessionID = message.chat.id
        result = sessionManager.addSession(sessionID, username, pwd)
        if result:
            bot.send_message(message.chat.id, "ай малаца")
        else:
            bot.send_message(message.chat.id, "пащел нахуй")
    else:
        bot.send_message(message.chat.id, "incorrect format")
