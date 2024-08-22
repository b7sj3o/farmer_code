from dotenv import load_dotenv
from os import getenv
from telebot import apihelper
load_dotenv()


TOKEN = getenv("BOT_TOKEN")
FASTAPI_HOST_LOCAL = getenv("FASTAPI_HOST_LOCAL")
FASTAPI_PORT_LOCAL = getenv("FASTAPI_PORT_LOCAL")

BASE_URL_LOCAL = f"http://{FASTAPI_HOST_LOCAL}:{FASTAPI_PORT_LOCAL}"

FASTAPI_URL_REGISTER = f"{BASE_URL_LOCAL}/register"
FASTAPI_URL_EXISTING_USER = f"{BASE_URL_LOCAL}/existing_user"
FASTAPI_URL_LOGIN_RESPONSE = f"{BASE_URL_LOCAL}/login_response"