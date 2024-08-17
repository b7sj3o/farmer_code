from dotenv import load_dotenv
from os import getenv
load_dotenv()


TOKEN = getenv("BOT_TOKEN")
BOT_HOST_CONTAINER = getenv("BOT_HOST_CONTAINER")
BOT_PORT_CONTAINER = getenv("BOT_PORT_CONTAINER")

BASE_URL_CONTAINER = f"http://{BOT_HOST_CONTAINER}:{BOT_PORT_CONTAINER}"

BOT_URL_VERIFICATION_LOGIN = f"{BASE_URL_CONTAINER}/bot_login_confirmation"