from fastapi import APIRouter
from crud.message import Message
from schemas.message import Message, MessageInDB


router = APIRouter(prefix="/message")

N = 10


@router.get("last/{chat_id}", response_model=MessageInDB)
async def get_messages(message: Message):
    pass


@router.post("", response_model=MessageInDB)
async def create_message(message: Message):
    user_db = MessageInDB(id=len(message_database) + 1, **message.dict())
    return user_db


@router.put("/{message_id}", response_model=MessageInDB)
async def update_chat(message_id: int, message: Message):
    user_db = message_database[message_id - 1]
    for param, value in message.dict().items():
        user_db[param] = value

    return user_db


@router.delete("/{message_id}")
async def delete_chat(message_id: int):
    db = list(message_database)
    del db[message_id - 1]
