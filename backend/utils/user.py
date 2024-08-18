from config.urls import TELEGRAM_API, TOKEN
from database.models.user import User

from telebot import types
import requests


def send_confirmation(user: User):
    bot_url = f"{TELEGRAM_API}/bot{TOKEN}/sendMessage"

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    button_confirm = types.InlineKeyboardButton("Confirm ✅", callback_data="confirm")
    button_cancel = types.InlineKeyboardButton("This is not me ❌", callback_data="cancel")
    keyboard.add(button_confirm, button_cancel)

    response = requests.post(
        bot_url,
        json={
            "chat_id": user.chat_id,
            "text": "Someone tried to log in into your account, please confirm to be sure that this is you",
            "reply_markup": keyboard.to_dict()
        }
    )

    # TODO: check response for success 



def get_username_by_chat_id(chat_id: int):
    bot_url = f"{TELEGRAM_API}/bot{TOKEN}/getChat"

    response = requests.post(
        bot_url,
        json={
            "chat_id": chat_id
        }
    )

    # TODO: check response for success 

    return response.json().get("result").get("username")