from config import bot
from telebot import types

# @bot.message_handler(commands=["msgbuttons"])
# def show_message_buttons(message):
#     button_confirm = types.InlineKeyboardButton('Confirm ✅', callback_data='foo')
#     button_cancel = types.InlineKeyboardButton('This is not me ❌', callback_data='bar')

#     keyboard = types.InlineKeyboardMarkup()
#     keyboard.add(button_confirm)
#     keyboard.add(button_cancel)

#     bot.send_message(message.chat.id, text='Someone tried to log in into your account, please confirm to be sure that this is you', reply_markup=keyboard)