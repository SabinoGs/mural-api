from sqlalchemy import Column, ForeignKey, String, Boolean, Integer

from mural_api.sql.config import Base

class User(Base):
    __tablename__ = "user_account"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    cpf = Column(String(11))
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name}, email={self.email}, cpf={self.cpf}"

