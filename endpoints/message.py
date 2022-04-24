from fastapi import APIRouter
from crud.message import message_database
from schemas.message import Message, MessageInDB


router = APIRouter(prefix="/message")


@router.post("", response_model=MessageInDB)
async def create_message(message: Message):
    """Создать пользователя"""
    # Здесь происходит добавление пользователя в БД
    user_db = MessageInDB(id=len(message_database) + 1, **message.dict())
    return user_db


@router.put("/{message_id}", response_model=MessageInDB)
async def update_chat(message_id: int, message: Message):
    user_db = message_database[message_id - 1]
    for param, value in message.dict().items():
        user_db[param] = value
        # здесь изменения сохраняются в базу

    return user_db


@router.delete("/{message_id}")
async def delete_chat(message_id: int):
    db = list(message_database)
    del db[message_id - 1]
