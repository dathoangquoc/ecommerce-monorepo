from pydantic import BaseModel


class User(BaseModel):
    id: str
    username: str
    email: str
    hashed_password: str


class UserIn(BaseModel):
    pass


class UserOut(BaseModel):
    pass


class Token(BaseModel):
    pass