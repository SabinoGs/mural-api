from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

from mural_api.settings import settings

DATABASE_URL = settings['DATABASE_URL']

engine = create_async_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
Base = declarative_base()
async_session_maker = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

