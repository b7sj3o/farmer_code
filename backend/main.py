from app import app
from routes import *
from database import engine, Base
import uvicorn

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9090)