from config import bot, FASTAPI_URL_EXISTING_USER, FASTAPI_URL_REGISTER
import requests

register_pressed = False


@bot.message_handler(commands=["register"])
def register(message):
    global register_pressed

    response = requests.post(f"{FASTAPI_URL_EXISTING_USER}", json={"chat_id": message.chat.id})
    result = response.json()

    if result.get("has_account"):
        bot.reply_to(message, result.get("message"))
    else:
        register_pressed = True

        bot.reply_to(message, "Choose username")



@bot.message_handler(func=lambda message: not message.text.startswith('/') and register_pressed)
def register_username(message):
    global register_pressed

    chat_id = message.chat.id
    username = message.text

    response = requests.post(FASTAPI_URL_REGISTER, json={
        "chat_id": chat_id,
        "username": username
    })

    if response.status_code == 200:
        bot.reply_to(message, response.json().get("message"))
        register_pressed = False
    else:
        bot.reply_to(message, f"Failed to register user: {response.content}")
   