import uuid
from typing import Any, Dict, Generic, List, Protocol, TypeVar, Optional
from fastapi import Depends

from fastapi_users_db_sqlalchemy import GUID
from sqlalchemy import Column, Integer, String, Float, select, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import Select

from mural_api.sql.config import Base, get_async_session

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
        ...

ICP = TypeVar("ICP", bound=InformativeCardProtocol)

def get_card_db(session: AsyncSession = Depends(get_async_session)):
    yield InformativeCardDataBase(session, InformativeCard)

class InformativeCardDataBase(Generic[ICP, ID]):
    """
    Database adapter to for SQLAlchemy
    """

    session: AsyncSession
    table: InformativeCardProtocol[ID]

    def __init__(self, session: AsyncSession, table: InformativeCardProtocol) -> None:
        self.session = session
        self.table = table

    async def get(self, id: ID) -> Optional[ICP]:
        statement = select(self.table).where(self.table.id == id)
        return await self._get_card(statement)

    async def fetch(self, limit: int) -> Optional[List[ICP]]:
        statement = select(self.table).limit(limit)
        result = await self._run_statement(statement)
        return [row[0] for row in result.all()]

    
    async def create(self, create_dict: Dict[str, Any]) -> ICP:
        card = self.table(**create_dict)
        self.session.add(card)
        await self.session.commit()
        await self.session.refresh(card)
        return card

    async def _run_statement(self, statement: Select):
        result = await self.session.execute(statement)
        return result

    async def _get_card(self, statement: Select) -> Optional[ICP]:
        result = await self._run_statement(statement)
        card = result.one()
        
        if card is None:
            return None
        
        return card[0]