from pydantic import BaseModel


class ConfirmRequest(BaseModel):
    chat_id: int


class UserCreate(BaseModel):
    chat_id: int
    username: str