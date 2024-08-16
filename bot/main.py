import telebot
import os
import requests
from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv("BOT_TOKEN")
FASTAPI_URL = "http://0.0.0.0:9090/register"
bot = telebot.TeleBot(TOKEN)
register_pressed = False


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    print(message.from_user)
    # bot.reply_to(message, "Hello! Send me a message and I will tell you your chat ID.")


@bot.message_handler(commands=["register"])
def register_user(message):
    global register_pressed

    register_pressed = True

    bot.reply_to(message, "Choose username")

@bot.message_handler(func=lambda message: not message.text.startswith('/') and register_pressed)
def register_username(message):
    chat_id = message.chat.id
    username = message.text

    response = requests.post(FASTAPI_URL, json={
        "chat_id": chat_id,
        "username": username
    })

    if response.status_code == 200:
        bot.reply_to(message, response.json().get("message"))
    else:
        bot.reply_to(message, f"Failed to register user: {response.content}")
    

bot.infinity_polling()


