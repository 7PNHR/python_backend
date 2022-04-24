from fastapi import APIRouter
from crud.user import user_databases
from schemas.user import User, UserInDB

router = APIRouter(prefix="/user")


@router.get("/{user_id}")
def get_user(user_id: int):
    """Получить пользоветеля по заданному user_id"""
    return user_databases[user_id - 1]


@router.post("", response_model=UserInDB)
async def create_user(user: User):
    """Создать пользователя"""
    # Здесь происходит добавление пользователя в БД
    user_db = UserInDB(id=len(user_databases) + 1, **user.dict())
    return user_db


@router.put("/{user_id}", response_model=UserInDB)
async def update_user(user_id: int, user: User):
    user_db = user_databases[user_id - 1]
    for param, value in user.dict().items():
        user_db[param] = value
        # здесь изменения сохраняются в базу

    return user_db


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    db = list(user_databases)
    del db[user_id-1]
