from fastapi import APIRouter
from crud.message import Message
from schemas.message import Message, MessageInDB


router = APIRouter(prefix="/message")


@router.get("last/{chat_id}/{message_count}")
async def find_last(chat_id: int, message_count: int):
    messages = []
    for value in message_database:
        print(value)
        if value.get("chat_id") == chat_id:
            messages.append(value)
    messages.sort(reverse=True, key=filter_message)
    messages = messages[:message_count]
    messages.reverse()
    return messages


def filter_message(e):
    return e.get("id")


@router.post("", response_model=MessageInDB)
async def create_message(message: Message):
    """Создать сообщение"""
    # Здесь происходит добавление пользователя в БД
    user_db = MessageInDB(id=len(message_database) + 1, **message.dict())
    return user_db


@router.put("/{message_id}", response_model=MessageInDB)
async def update_message(message_id: int, message: Message):
    user_db = message_database[message_id - 1]
    for param, value in message.dict().items():
        user_db[param] = value

    return user_db


@router.delete("/{message_id}")
async def delete_message(message_id: int):
    db = list(message_database)
    del db[message_id - 1]
