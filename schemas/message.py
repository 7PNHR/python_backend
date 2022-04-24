from pydantic import BaseModel
from datetime import datetime


class Message(BaseModel):
    text: str
    creation_date: datetime
    is_updated: bool
    update_date: datetime
    is_viewed: bool
    media: list


# media - ссылки на ресурс


class MessageInDB(Message):
    id: int
    chat_id: int
