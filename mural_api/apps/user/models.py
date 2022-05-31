from mural_api.sql.config import Base
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(SQLAlchemyBaseUserTableUUID, Base):
    name = Column(String(150))
    email = Column(String(50))

    cards = relationship("InformativeCard", back_populates="user")