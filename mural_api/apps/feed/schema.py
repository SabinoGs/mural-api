import datetime
from . import models
from typing import Generic, Optional
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
    title: str
    description: str
    price: Optional[float]
    user_id: models.ID

class InformativeCardRead(BaseInformativeCard):

    created_at: Optional[datetime.datetime]
    
    class Config:
        orm_mode = True

class InformativeCardUpdate(BaseInformativeCard, InformativeCardUpdateDictModel):
    pass

class InformativeCardCreate(InformativeCardUpdateDictModel):
    user_id: models.ID
    title: str
    description: str
    price: Optional[float]