from . import models
from typing import Generic
from pydantic import BaseModel


class InformativeCardUpdateDictModel(BaseModel):
    def create_update_dict(self):
        return self.dict(
            exclude_unset=True,
            exclude={
                "user",
            }
        )

class BaseInformativeCard(Generic[models.ID], BaseModel):
    id: models.ID
    user_id: models.ID
    title: str
    description: str
    price: float

class InformativeCardRead(BaseInformativeCard):
    pass

class InformativeCardUpdate(BaseInformativeCard, InformativeCardUpdateDictModel):
    pass

class InformativeCardCreate(BaseInformativeCard, InformativeCardUpdateDictModel):
    pass