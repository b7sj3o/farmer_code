import telebot
import os
import requests

from config import bot
from handlers.register import register, register_username



# def register_handlers():
#     bot.register_message_handler(register, commands=["register"])
#     bot.register_message_handler(register_username)


def run():
    # register_handlers()
    bot.infinity_polling()


run()


