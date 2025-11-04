"""
FastAPI endpoints
"""
from fastapi import APIRouter

from .models import ProductCreate, ProductRead
from .service import CatalogService


router = APIRouter(prefix="/catalog")


@router.get("/")
def read_catalog(service: CatalogService, limit: int = 10):
    return "All items here"


@router.get("/{product_id}", response_model=ProductRead)
def read_product(service: CatalogService, product_id: str):
    return {"product_id": product_id}
