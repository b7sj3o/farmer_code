import requests
from fastapi import HTTPException

from database.models.user import User
from database.connection import Session
from app import app
from config import UserCreate, CheckUserChatID, CheckUserUsername, BOT_URL_VERIFICATION_LOGIN

@app.get("/")
def home():
    response = requests.post(
        BOT_URL_VERIFICATION_LOGIN,
        json={
            "chat_id": 928132950
        }
    )
    print(response)

@app.post("/existing_user")
def existing_user(user: CheckUserChatID):
    with Session() as db:
        existing_user = db.query(User).filter(User.chat_id == user.chat_id).first()
        if existing_user:
            return {
                "message": "You already have account",
                "has_account": True
                }


        return {
            "message": "You don't have account",
            "has_account": False
        }


@app.post("/login_user")
def login_user(user: CheckUserUsername):
    with Session() as db:
        user = db.query(User).filter(User.username == user.username).first()
        if not user:
            return HTTPException(status_code=404, detail={
                "message": "User not found",
                "success": False
            })

        chat_id = user.chat_id
        response = requests.post()
        if response:
            user.authenticated = True
            db.commit()
        
            return {
                "message": "Login confirmed",
                "success": True
            }
        else:
            return {
                "message": "Confirmation failed",
                "success": False
            }


@app.post("/register")
def register_user(user: UserCreate):
    with Session() as db:
        if existing_user(user):
            new_user = User(
                chat_id=user.chat_id,
                username=user.username,
            )

            db.add(new_user)
            db.commit()
            db.refresh(new_user)

            return {"message": "User has been registred successfully"}
        

