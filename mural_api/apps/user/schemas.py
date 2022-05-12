import uuid
from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    email: str
    name: str


class UserCreate(schemas.BaseUserCreate):
    email: str
    name: str


class UserUpdate(schemas.BaseUserUpdate):
    email: str
    name: str