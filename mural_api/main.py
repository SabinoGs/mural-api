import uuid
from typing import List

from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers

from mural_api.apps.user.models import Base
from mural_api.apps.user.schemas import UserCreate, UserRead, UserUpdate 
from mural_api.apps.user.models import User

from mural_api.authentication.manager import get_user_manager
from mural_api.authentication.backend import auth_backend

from mural_api.apps.feed.urls import create_card_router

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

current_active_user = fastapi_users.current_user(active=True)


app = FastAPI()
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"]
)

app.include_router(
    create_card_router(current_active_user)
)

@app.get("/")
def root(user: User = Depends(current_active_user)):
    return {"message": "Hello World"}


# @app.on_event("startup")
# async def on_startup():
#     await create_db_and_tables()