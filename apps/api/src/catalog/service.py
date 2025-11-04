"""
Business logic

Uses the repository abstraction ad FastAPI dependency injection for the session
"""

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..db.session import get_db
from .models import ProductCreate, ProductRead
from .repositories import ProductRepository


class CatalogService:
    def __init__(self, db: AsyncSession = Depends(get_db)):
        self.repo = ProductRepository(db)
    
    async def read_catalog(self):
        return await self.repo.read_all()
    
    async def read_product(self, product_id: str):
        return await self.repo.read(str)
    
    async def create_product(self, product: ProductCreate):
        raise await self.repo.create(product)