"""
Data access layer

Uses the session provided by db/session.py
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .schemas import Product


class ProductRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def read_all(self):
        result = await self.session.execute(select(Product))
        return result.scalars().all()
    
    async def read(self, product_id: str):
        result = await self.session.get(Product, product_id)
        return result
    
    async def update(self, product: Product):
        raise NotImplementedError
    
    async def delete(self, product: Product):
        obj = await self.read(product)
        await self.session.delete(obj)

    async def create(self, product: Product):
        self.session.add(product)
        await self.session.commit()