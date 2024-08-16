from database.models.user import User
from database.connection import Session
from app import app
from config import *



db = Session()

@app.get("/")
def home():
    return {"message": "HELLO"}

@app.post("/confirm_login")
def confirm_login(request: ConfirmRequest):
    user = db.query(User).filter(User.chat_id == request.chat_id).first()
    if not user:
        {"message": "User not found"}
    
    return {"message": "Login confirmed"}


@app.post("/register")
def register_user(request: UserCreate):
    existing_user = db.query(User).filter(User.chat_id == request.chat_id).first()
    if existing_user:
        db.close()
        return {"message": "User has account"}
    
    new_user = User(
        chat_id=request.chat_id,
        username=request.username,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()

    return {"message": "User has been registred successfully"}
    