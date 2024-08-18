from config import bot


@bot.message_handler(commands=["start"])
def home(message):
    bot.reply_to(message, f"Hello, {message.from_user.first_name}")