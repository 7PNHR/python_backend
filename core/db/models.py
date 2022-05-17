from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String)
    password = Column(String)
    name = Column(String)


class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    creation_date = Column(DateTime, server_default=func.now())
    type = Column(Integer, ForeignKey('chat_types.id'))


class UserChat(Base):
    __tablename__ = "users_chats"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    chat_id = Column(Integer, ForeignKey('chats.id'))


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer, ForeignKey('chats.id'))
    text = Column(String)
    creation_date = Column(DateTime)
    is_updated = Column(Boolean)
    update_date = Column(DateTime)
    is_viewed = Column(Boolean)
    is_deleted = Column(Boolean)


class ChatType(Base):
    __tablename__ = "chat_types"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
