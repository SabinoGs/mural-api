from fastapi_users_db_sqlalchemy import GUID
from pydantic import BaseModel
from sqlalchemy import Float


class InformativeCardUpdateDictModel(BaseModel):
    def create_update_dict(self):
        return self.dict(
            exclude_unset=True,
            exclude={
                "user",
            }
        )

class BaseInformativeCard(BaseModel):
    id: GUID
    user_id: GUID
    title: str
    description: str
    price: Float

class InformativeCardRead(BaseInformativeCard):
    pass

class InformativeCardUpdate(BaseInformativeCard, InformativeCardUpdateDictModel):
    pass

class InformativeCardCreate(BaseInformativeCard, InformativeCardUpdateDictModel):
    pass