from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from mural_api.settings import settings

DATABASE_URL = settings['DATABASE_URL']

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
