import uuid
from fastapi import Depends
from fastapi_users import BaseUserManager, UUIDIDMixin
from mural_api.apps.user.dependency import get_user_db
from mural_api.apps.user.models import User
from mural_api.settings import settings

SECRET_KEY = settings['SECRET_KEY']

class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET_KEY
    verification_token_secret = SECRET_KEY

def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
