from unicodedata import name
from sqlalchemy.orm import Session

from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(db: Session, user: schemas.UserCreate):
    to_create = models.User(
        email=user.email,
        password=user.password,
        cpf=user.cpf,
        name=user.name
    )

    db.add(to_create)
    db.commit()
    db.refresh(to_create)
    return to_create