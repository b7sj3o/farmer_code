from config import bot
from telebot import types
import requests
from config import FASTAPI_URL_LOGIN_RESPONSE

button_confirm_text = "Confirm ✅"
button_cancel_text = "This is not me ❌"

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    print(f"{call=}")
    if call.data == "confirm":
        response = requests.post(FASTAPI_URL_LOGIN_RESPONSE, json={
            "success": True,
            "chat_id": call.message.chat.id # TODO: look how call looks inside
        })

        # TODO: check response for success 


        bot.answer_callback_query(call.id, "You have confirmed your login.")
        bot.send_message(call.message.chat.id, "Login confirmed.")
    elif call.data == "cancel":
        response = requests.post(FASTAPI_URL_LOGIN_RESPONSE, json={
            "success": False
        })

        # TODO: check response for success 

        bot.answer_callback_query(call.id, "Login cancelled.")
        bot.send_message(call.message.chat.id, "Login cancelled.")