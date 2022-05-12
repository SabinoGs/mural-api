from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, ForeignKey, String, Boolean, Integer

from mural_api.sql.config import Base

class User(SQLAlchemyBaseUserTableUUID, Base):
    name = Column(String(150))
    email = Column(String(50))

