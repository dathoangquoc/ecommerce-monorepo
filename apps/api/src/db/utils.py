"""
Database initialization, seed data, cleanup scripts.
"""

from .base import Base
from .engine import engine, session_maker
from ..catalog.schemas import Product


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

mock_data = [
    Product(
        name="Product 1",
        price=100,
        description="Lorem ipsum",
        count=1
    ),
    Product(
        name="Product 2",
        price=200,
        description="Lorem ipsum",
        count=2
    ),
    Product(
        name="Product 3",
        price=300,
        description="Lorem ipsum",
        count=3
    )
]

async def seed_data():
    async with session_maker.begin() as session:
        session.add_all(mock_data)
        await session.commit()