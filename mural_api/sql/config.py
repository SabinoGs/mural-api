from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from mural_api.settings import settings

DATABASE_URL = settings['DATABASE_URL']

engine = create_async_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)
Base = declarative_base()
async_session_maker = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
