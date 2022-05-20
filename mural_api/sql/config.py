from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from mural_api.settings import settings

DATABASE_URL = settings['DATABASE_URL']

engine = create_engine(
    DATABASE_URL,
    future=True,
    connect_args={"check_same_thread": False},
)
Base = declarative_base()
session_maker = sessionmaker(bind=engine, expire_on_commit=False)


# async def create_db_and_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)

