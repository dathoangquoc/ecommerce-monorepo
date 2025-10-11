from datetime import datetime, timedelta, timezone

from pwdlib import PasswordHash
import jwt

from .config import settings


hasher = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return hasher.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return hasher.verify(plain, hashed)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()

    # Set default token expiration time
    now = datetime.now(timezone.utc)
    if expires_delta:
        expire = now + expires_delta
    else:
        expire = now + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    # JWT 'exp' should be a NumericDate (int seconds since epoch)
    to_encode.update({"exp": int(expire.timestamp())})

    # Encode a payload into JWT
    encoded_jwt = jwt.encode(
        payload=to_encode,
        key=settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )

    return encoded_jwt


def decode_token(token: str) -> str:
    jwt.decode(token, settings.JWT_SECRET_KEY, [settings.JWT_ALGORITHM])
