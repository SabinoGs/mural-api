from mural_api.sql.config import Base
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, String


class User(SQLAlchemyBaseUserTableUUID, Base):
    name = Column(String(150))
    email = Column(String(50))
