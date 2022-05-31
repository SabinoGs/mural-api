import uuid
from fastapi_users_db_sqlalchemy import GUID, ForeignKey
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from mural_api.sql.config import Base


class InformativeCard(Base):

    __tablename__ = "informative_card"

    id = Column(GUID, primary_key=True, default=uuid.uuid4)
    title = Column(String(length=256), nullable=False)
    description = Column(String(length=512), nullable=True)
    price = Column(Float, nullable=True)

    user_id = Column(GUID, ForeignKey('user.id'))
    user = relationship("User", back_populates="cards")
