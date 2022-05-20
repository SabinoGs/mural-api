from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.orm import Session
from mural_api.apps.user.models import User
from mural_api.sql.config import session_maker

def get_session():
    db = session_maker()
    try:
        yield db
    finally:
        db.close()    

def get_user_db(session: Session = Depends(get_session)):
    yield SQLAlchemyUserDatabase(session, User)