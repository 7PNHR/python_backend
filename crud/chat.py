from sqlalchemy.orm import Session
from core.db.models import Chat, UserChat
import schemas.chat as schema


def create_chat(db: Session, chat: schema.Chat):
    chat_db = Chat(**chat.dict())
    db.add(chat_db)
    db.commit()
    return chat_db


def get_chat_by_id(db: Session, chat_id: int):
    return db.query(Chat).filter(Chat.id == chat_id).one_or_none()


def update_chat(db: Session, chat_id: int, name: str):
    chat_db = db.query(Chat).filter(Chat.id == chat_id).one_or_none()
    setattr(chat_db, "name", name)
    db.commit()
    return chat_db


def delete_chat(db: Session, chat_id: int):
    db.query(UserChat).filter(UserChat.chat_id == chat_id).delete()
    db.query(Chat).filter(Chat.id == chat_id).delete()
    db.commit()


