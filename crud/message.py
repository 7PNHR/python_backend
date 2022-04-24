from datetime import datetime

message_database = [
    {
        "id": 1,
        "chat_id": 1,
        "text": "Привет",
        "creation_date": datetime(2022, 4, 20, 19, 39, 0),
        "is_updated": False,
        "update_date": None,
        "is_viewed": False,
        "media": []
    },
    {
        "id": 2,
        "chat_id": 1,
        "text": "Мир!",
        "creation_date": datetime(2022, 4, 20, 19, 40, 0),
        "is_updated": True,
        "update_date": datetime(2022, 4, 20, 19, 41, 0),
        "is_viewed": False,
        "media": []
    }
]
# media это картиночки, видосики и прочая шляпа
