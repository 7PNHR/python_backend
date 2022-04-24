from datetime import datetime
from pydantic import BaseModel
from enum import Enum


class ChatType(str, Enum):
    public = "public"
    private = "private"
    group = "group"


class Chat(BaseModel):
    name: str
    creation_date: datetime
    type: ChatType


class ChatInDB(Chat):
    id: int

