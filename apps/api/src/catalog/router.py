"""
FastAPI endpoints
"""

from fastapi import APIRouter, Depends

from .models import ProductCreate, ProductRead
from .service import CatalogService


router = APIRouter(prefix="/catalog")


@router.get("/", response_model=list[ProductRead])
async def read_catalog(service: CatalogService = Depends(), limit: int = 10):
    return await service.read_catalog()


@router.get("/{product_id}", response_model=ProductRead)
async def read_product(service: CatalogService, product: ProductRead):
    return await service.read_product(product)
