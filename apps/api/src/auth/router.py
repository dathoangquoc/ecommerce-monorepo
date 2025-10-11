from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from . import schemas, service, dependencies
from .utils import hash_password

router = APIRouter(prefix="/auth")


@router.post("/register")
async def register_user(user_in: schemas.User):
    return service.register_user(user_in)


@router.post("/login")
async def login_user(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return service.login_user(form_data)


@router.get("/me")
def read_me(
    current_user: Annotated[schemas.User, Depends(dependencies.get_current_user)],
):
    return current_user


# FOR TESTING ONLY
@router.get("/hash")
def read_hash(password: str):
    return hash_password(password)
