from app import app
from routes import *
from database import engine, Base
import uvicorn
from config import FASTAPI_HOST_CONTAINER, FASTAPI_PORT_CONTAINER

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run(app, host=FASTAPI_HOST_CONTAINER, port=FASTAPI_PORT_CONTAINER)