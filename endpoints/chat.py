from fastapi import APIRouter
from crud.chat import chat_database, user_chat_database
from crud.message import message_database
from schemas.chat import Chat, ChatInDB

router = APIRouter(prefix="/chat")

N = 10


@router.get("last/{chat_id}", response_model=ChatInDB)
async def create_chat(user: Chat):
    pass


'''
def filter():
    lastMessages = list(message_database)
    filter(filter_by_chat_id,message_database)
    lastMessages.sort(key=lastMessages.)
    return
'''


@router.get("/{chat_id}")
def get_chat(chat_id: int):
    """Получить чат по заданному user_id и список участников"""
    user_list = list()
    for value in user_chat_database:
        if value.get("chat_id") == chat_id:
            user_list.append(value.get("user_id"))
    return [chat_database[chat_id - 1], user_list]


@router.post("", response_model=ChatInDB)
async def create_chat(chat: Chat):
    """Создать пользователя"""
    # Здесь происходит добавление пользователя в БД
    user_db = ChatInDB(id=len(chat_database) + 1, **chat.dict())
    return user_db


@router.put("/{chat_id}", response_model=ChatInDB)
async def update_chat(chat_id: int, chat: Chat):
    user_db = chat_database[chat_id - 1]
    for param, value in chat.dict().items():
        user_db[param] = value
        # здесь изменения сохраняются в базу

    return user_db


@router.delete("/{chat_id}")
async def delete_chat(chat_id: int):
    db = list(chat_database)
    del db[chat_id - 1]
