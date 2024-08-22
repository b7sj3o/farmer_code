import requests
from fastapi import HTTPException, Response
from telebot import types
from typing import Optional

from database.models.user import User
from database.connection import Session
from app import app
from config.pydantic_models import UserCreate, CheckUserChatID, CheckUserUsername, LoginResponse
from config.urls import TOKEN, TELEGRAM_API
from utils.user import send_confirmation, get_username_by_chat_id


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


@app.post("/login_user")
def login_user(user: CheckUserUsername):
    with Session() as db:
        user = db.query(User).filter(User.username == user.username).first()
        if not user:
            return {
                "message": "User not found",
                "success": False
            }

        if user.authenticated:
            return {
                "user": user
            }

        send_confirmation(user)
        telegram_username = get_username_by_chat_id(user.chat_id)


        return {
                "message": f"Confirmation sent to telegram: @{telegram_username}",
                "success": True
            }


@app.post("/login_response")
def login_response(data: LoginResponse):
    with Session() as db:
        user = db.query(User).filter(User.chat_id == data.chat_id).first() # TODO: create func find_user() in utils
        user.responsed = True
        if data.success:
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


@app.get("/get_user")
def get_user(username: str):
    with Session() as db:
        user = db.query(User).filter(User.username == username).first()

        if user and user.responsed:
            if user.authenticated:
                return {"message": "User Loginned successfully", "status_code": 200, "user": user}
            elif not user.confirmed:
                return {"message": "User not confirmed", "status_code": 401}

        elif not user:
            return {"message": "User not found", "status_code": 404}
