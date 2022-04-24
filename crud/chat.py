from datetime import datetime
from schemas.chat import ChatType


chat_database = [
    {
        "id": 1,
        "name": "Чат 1",
        "creation_date": datetime(2022, 4, 20, 19, 39, 0),
        "type": ChatType.private
    }
]

user_chat_database = [
    {
        "user_id": 1,
        "chat_id": 1
    },
    {
        "user_id": 2,
        "chat_id": 1
    }
]
