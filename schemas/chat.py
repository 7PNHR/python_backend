from datetime import datetime
from pydantic import BaseModel


class Chat(BaseModel):
    name: str
    creation_date: datetime
    type: str


class ChatInDB(Chat):
    id: int

    class Config:
        orm_mode = True

