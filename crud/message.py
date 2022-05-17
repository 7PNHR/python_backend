from sqlalchemy.orm import Session
from core.db.models import Message
import schemas.message as schema


def create_message(db: Session, chat: schema.Message):
    message_db = Message(**chat.dict())
    db.add(message_db)
    db.commit()
    return message_db


def get_message_by_id(db: Session, message_id: int):
    return db.query(Message).filter(Message.id == message_id).one_or_none()


def update_message(db: Session, message_id: int, message: schema.Message):
    message_db = db.query(Message).filter(Message.id == message_id).one_or_none()
    for param, value in message.dict().items():
        setattr(message_db, param, value)
    db.commit()
    return message_db


def delete_chat(db: Session, message_id: int):
    message_db = db.query(Message).filter(Message.id == message_id).one_or_none()
    setattr(message_db, "is_deleted", True)
    db.commit()