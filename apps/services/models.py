from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    is_available: bool


class User(BaseModel):
    username: str
    email: str | None = None
    hashed_password: str | None = None

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None