"""
FastAPI endpoints
"""

from fastapi import APIRouter, Depends

from .models import ProductCreate, ProductRead, ProductUpdate
from .service import CatalogService


router = APIRouter(prefix="/catalog")


@router.get("/", response_model=list[ProductRead])
async def read_catalog(service: CatalogService = Depends(), limit: int = 10):
    return await service.read_catalog()


@router.get("/{product_id}", response_model=ProductRead)
async def read_product(product_id: str, service: CatalogService = Depends()):
    return await service.read_product(product_id)


@router.post("/")
async def create_product(product: ProductCreate, service: CatalogService = Depends()):
    return await service.create_product(product)


@router.put("/")
async def update_product(product: ProductUpdate, service: CatalogService = Depends()):
    return await service.update_product(product)