"""
Data access layer

Uses the session provided by db/session.py
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .schemas import Product
from .models import ProductCreate, ProductUpdate

class ProductRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, product: ProductCreate) -> Product | None:
        product = Product(**product.model_dump())
        self.session.add(product)
        await self.session.commit()
        return product
    
    async def read_all(self) -> list[Product]:
        result = await self.session.execute(select(Product))
        return result.scalars().all()
    
    async def read(self, product_id: str) -> Product | None:
        result = await self.session.get(Product, product_id)
        return result
    
    async def update(self, product: ProductUpdate) -> Product | None:
        prev_product = await self.read(product.id)
        if not prev_product:
            return None
        
        for k, v in product.model_dump(exclude_unset=True).items():
            setattr(prev_product, k, v)

        await self.session.commit()
        await self.session.refresh(prev_product)
        return prev_product

    async def delete(self, product: Product) -> Product | None:
        obj = await self.read(product)
        await self.session.delete(obj)

    