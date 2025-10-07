import os
from datetime import datetime, timedelta, timezone
from typing import Annotated

from dotenv import load_dotenv

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

import jwt
from jwt.exceptions import InvalidTokenError

from pwdlib import PasswordHash

from models import User, Token, TokenData

# Load env
load_dotenv("../.env")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(prefix="/auth")

# Expose a /token endpoint to generate access tokens
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


user_db = {
    "john": {
        "username": "John Cornelious",
        "email": "john@email.com",
        "hashed_password": "hashedsecret"
    }
}

hasher = PasswordHash.recommended()


def authenticate_user(username: str, password: str):
    user = get_user_from_db(username)
    
    # Check if user is in DB
    if not user:
        return None
    
    # Check if password matches the hash
    if hasher.verify(password, user.hashed_password):
        return None
    
    return user
    

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()

    # Set default token expiration time
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    # Encode a payload into JWT
    encoded_jwt = jwt.encode(
        payload=to_encode,
        key=SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


def get_user_from_db(username: str):
    return user_db[username] 


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # Decode JWT    
    try:
        payload = jwt.decode(
            jwt=token,
            key=SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        username = payload.get("sub")
        if username is None:
            raise
        token_data = TokenData(username)
    except InvalidTokenError:
        raise credentials_exception
    
    user = get_user_from_db(token_data.username)
    if not user:
        raise credentials_exception
    
    return user


@router.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:        
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    payload = {"sub": user.username}
    access_token = create_access_token(data=payload)

    return Token(access_token, token_type="bearer")

@router.get("/me")
def read_me(
    current_user: Annotated[User, Depends(get_current_user)]
):
    return [{
        "item_id" : "Phone",
        "owner": current_user.username
    }]