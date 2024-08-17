from dotenv import load_dotenv
from os import getenv
load_dotenv()

IMG_BLOCK = "frontend/assets/images/dirt.png"

FASTAPI_HOST_LOCAL = getenv("FASTAPI_HOST_LOCAL")
FASTAPI_PORT_LOCAL = getenv("FASTAPI_PORT_LOCAL")
BASE_URL_LOCAL = f"http://{FASTAPI_HOST_LOCAL}:{FASTAPI_PORT_LOCAL}"

FASTAPI_URL_LOGIN = f"{BASE_URL_LOCAL}/login_user"