from fastapi import Depends
from fastapi_users_db_sqlalchemy import AsyncSession, SQLAlchemyUserDatabase
from mural_api.apps.user.models import User

from mural_api.sql.config import get_async_session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)