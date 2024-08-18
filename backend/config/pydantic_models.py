from pydantic import BaseModel


class CheckUserUsername(BaseModel):
    username: str


class CheckUserChatID(BaseModel):
    chat_id: int


class UserCreate(BaseModel):
    chat_id: int
    username: str


class LoginResponse(BaseModel):
    chat_id: int
    success: bool

