from dotenv import load_dotenv
from os import getenv
load_dotenv()


FASTAPI_HOST_LOCAL = getenv("FASTAPI_HOST_LOCAL")
FASTAPI_PORT_LOCAL = getenv("FASTAPI_PORT_LOCAL")

BASE_URL_LOCAL = f"http://{FASTAPI_HOST_LOCAL}:{FASTAPI_PORT_LOCAL}"

FASTAPI_URL_LOGIN = f"{BASE_URL_LOCAL}/login_user"
FASTAPI_URL_GET_USER = f"{BASE_URL_LOCAL}/get_user"
FASTAPI_URL_HARVEST_RESOURCES = f"{BASE_URL_LOCAL}/harvest_resources"