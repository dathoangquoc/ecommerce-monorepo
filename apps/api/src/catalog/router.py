from fastapi import APIRouter

from .models import Item


router = APIRouter(prefix="/catalog")


@router.get("/")
def read_catalog(limit: int = 10):
    return "All items here"

@router.get("/{item_id}", response_model=Item)
def read_item(item_id: str):
    return {"item_id" : item_id}