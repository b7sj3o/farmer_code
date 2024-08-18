from dotenv import load_dotenv
from os import getenv
from telebot import apihelper
load_dotenv()


# apihelper.API_URL = "http://0.0.0.0:8001/bot{0}/{1}"

TOKEN = getenv("BOT_TOKEN")
FASTAPI_HOST_CONTAINER = getenv("FASTAPI_HOST_CONTAINER")
FASTAPI_PORT_CONTAINER = getenv("FASTAPI_PORT_CONTAINER")

BASE_URL_CONTAINER = f"http://{FASTAPI_HOST_CONTAINER}:{FASTAPI_PORT_CONTAINER}"

FASTAPI_URL_REGISTER = f"{BASE_URL_CONTAINER}/register"
FASTAPI_URL_EXISTING_USER = f"{BASE_URL_CONTAINER}/existing_user"
FASTAPI_URL_LOGIN_RESPONSE = f"{BASE_URL_CONTAINER}/login_response"