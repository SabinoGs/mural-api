import uuid
from typing import Any, Dict, Generic, Protocol, TypeVar

from fastapi_users_db_sqlalchemy import GUID, AsyncSession, ForeignKey
from pyparsing import Optional
from sqlalchemy import Column, Integer, String, Float, select
from sqlalchemy.orm import relationship
from sqlalchemy.sql import Select

from mural_api.sql.config import Base

ID = TypeVar("ID")
class InformativeCard(Base):

    __tablename__ = "informative_card"

    id = Column(GUID, primary_key=True, default=uuid.uuid4)
    title = Column(String(length=256), nullable=False)
    description = Column(String(length=512), nullable=True)
    price = Column(Float, nullable=True)

    user_id = Column(GUID, ForeignKey('user.id'))
    user = relationship("User", back_populates="cards")


class InformativeCardProtocol(Protocol[ID]):
    """
    Strutural model for InformativeCard
    """

    id: ID
    title: str
    description: str
    price: float
    user_id: uuid.uuid4

    def __init__(self) -> None:
        pass


class InformativeCardDataBase(Generic[ID]):
    """
    Database adapter to for SQLAlchemy
    """

    session: AsyncSession
    table: InformativeCardProtocol[ID]

    def __init__(self, session: AsyncSession, table: InformativeCardProtocol) -> None:
        self.session = session
        self.table = table

    async def get(self, id: ID) -> Optional[InformativeCardProtocol]:
        statement = select(self.table).where(self.table.id == id)
        return await self._get_card(statement)

    
    async def create(self, create_dict: Dict[str, Any]) -> InformativeCardProtocol:
        card = self.table(**create_dict)
        self.session.add(card)
        await self.session.commit()
        await self.session.refresh(card)
        return card

    async def _run_statement(self, statement: Select):
        result = await self.session.execute(statement)
        return result

    async def _get_card(self, statement: Select) -> Optional[InformativeCardProtocol]:
        result = self._run_statement(statement)
        card = result.first()
        
        if card is None:
            return None
        
        return card[0]