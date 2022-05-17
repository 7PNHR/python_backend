from fastapi import APIRouter, Depends, HTTPException, status
from deps import get_db
import crud.chat as crud
import crud.user as user_crud
from schemas.chat import Chat, ChatInDB

router = APIRouter(prefix="/chat")


@router.get("/{chat_id}")
def get_chat(chat_id: int, db=Depends(get_db)):
    """Получить чат по заданному user_id и список участников"""
    chat = crud.get_chat_by_id(db=db, chat_id=chat_id)
    users = user_crud.get_users_by_chat_id(db, chat_id)
    return [chat, users]


@router.post("", response_model=ChatInDB)
async def create_chat(chat: Chat, db=Depends(get_db)):
    """Создать чат"""
    result = crud.create_chat(db=db, chat=chat)
    return result


@router.put("/{chat_id}/{name}", response_model=ChatInDB)
async def update_chat(chat_id: int, name: str, db=Depends(get_db)):
    """Добавить участника в чат (если это группа)"""
    chat = crud.get_chat_by_id(db=db, chat_id=chat_id)
    if chat.type == 3:
        chat_db = crud.update_chat(db=db, chat_id=chat_id, name=name)
        return chat_db


@router.delete("/{chat_id}")
async def delete_chat(chat_id: int, db=Depends(get_db)):
    crud.delete_chat(db=db, chat_id=chat_id)
