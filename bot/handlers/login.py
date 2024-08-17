from config import bot
from telebot import types
# import requests

button_confirm_text = "Confirm ✅"
button_cancel_text = "This is not me ❌"

def bot_login_confirmation(chat_id: int):
    button_confirm = types.InlineKeyboardButton(f"{button_confirm_text}", callback_data="foo")
    button_cancel = types.InlineKeyboardButton(f"{button_cancel_text}", callback_data="bar")

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button_confirm)
    keyboard.add(button_cancel)

    bot.send_message(chat_id, text="Someone tried to log in into your account, please confirm to be sure that this is you", reply_markup=keyboard)

    return True

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == "confirm":
        bot.answer_callback_query(call.id, "You have confirmed your login.")
        bot.send_message(call.message.chat.id, "Login confirmed.")
    elif call.data == "cancel":
        bot.answer_callback_query(call.id, "Login cancelled.")
        bot.send_message(call.message.chat.id, "Login cancelled.")