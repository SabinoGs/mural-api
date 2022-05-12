from multiprocessing import AuthenticationError
from mural_api.settings import settings
from fastapi_users.authentication import BearerTransport, JWTStrategy, AuthenticationBackend



SECRET_KEY = settings["SECRET_KEY"]
SECRET_LIFETIME = int(settings["SECRET_LIFETIME"])

transport = BearerTransport(tokenUrl="auth/jwt/login")

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_KEY, lifetime_seconds=SECRET_LIFETIME)


auth_backend = AuthenticationBackend(name='jwt', transport=transport, get_strategy=get_jwt_strategy)