"""
Data access layer

Uses the session provided by db/session.py
"""

from .schemas import Product


class ProductRepository:
    def __init__(self):
        raise NotImplementedError

    async def read_all(self):
        raise NotImplementedError

    async def create(self, product: Product):
        raise NotImplementedError