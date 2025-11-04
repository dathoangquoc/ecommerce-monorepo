"""
Business logic

Uses the repository abstraction ad FastAPI dependency injection for the session
"""

from .models import ProductCreate


class CatalogService:
    def __init__(self):
        raise NotImplementedError
    
    async def read_catalog(self):
        raise NotImplementedError
    
    async def create_product(self, product: ProductCreate):
        raise NotImplementedError