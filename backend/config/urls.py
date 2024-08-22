from dotenv import load_dotenv
from os import getenv
load_dotenv()


TOKEN = getenv("BOT_TOKEN")
TELEGRAM_API = getenv("TELEGRAM_API")
FASTAPI_HOST_LOCAL = getenv("FASTAPI_HOST_LOCAL")
FASTAPI_PORT_LOCAL = int(getenv("FASTAPI_PORT_LOCAL"))