from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from .models import Token

from .utils import verify_password, create_access_token


async def register_user():
    pass


async def get_user_by_id(id: str):
    return user_db[id]


def authenticate_user(user_id: str, password: str):
    user = get_user_by_id(user_id)

    # Check if user is in DB
    if not user:
        return None

    # Check if password matches the hash
    if verify_password(plain=password, hashed=user.get("hashed_password")):
        return user

    return None


async def login_user(form_data: OAuth2PasswordRequestForm):
    # Authenticate user
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    # If correct, create an access token for the user
    username = user.get("username")
    payload = {"sub": username}
    access_token = create_access_token(data=payload)

    return Token(
        access_token=access_token,
        token_type="bearer",
    )
