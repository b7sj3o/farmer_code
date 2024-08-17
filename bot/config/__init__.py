from .config import TOKEN, FASTAPI_URL_EXISTING_USER, FASTAPI_URL_REGISTER
from telebot import TeleBot, apihelper

bot = TeleBot(token=TOKEN, num_threads=5)

# apihelper.ENABLE_MIDDLEWARE = True