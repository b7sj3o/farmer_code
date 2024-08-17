from app import app
from routes import *
from database import engine, Base
import uvicorn


# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)