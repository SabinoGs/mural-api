
from fastapi import Request
import uuid

from pyparsing import Optional
from fastapi_users_db_sqlalchemy import UP

from mural_api.apps.feed.models import ID, InformativeCardDataBase, InformativeCardProtocol
from mural_api.apps.feed.schema import InformativeCardCreate


class InformativeCardManager():
    """
    InformativeCard management logic. 
    Responsable for control the upper level data when receiving from or retrieving data to user

    :param card_db: Database adapter instance
    """

    def __init__(self, card_db: InformativeCardDataBase) -> None:
        self.card_db = card_db

    async def get(self, id: ID):
        """
        Get InformativeCard by id.

        :param id: Id. of a card
        :raises CardNotFound: The Card does not exist.
        :return: A card.
        """
        card = await self.card_db.get(id)

        if card is None:
            raise KeyError("Card Not found")

        return card

    async def create(
        self, 
        create_dict: InformativeCardCreate, 
        current_user: UP 
    ) -> InformativeCardProtocol:
        """
        Create a InformativeCard in database
        """

        create_dict.user_id = current_user.id
        card = await self.card_db.create(create_dict.create_update_dict())
        return card
