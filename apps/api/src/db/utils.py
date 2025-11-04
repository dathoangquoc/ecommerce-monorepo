"""
Database initialization, seed data, cleanup scripts.
"""

from .base import Base
from .engine import session_maker


async def init_db():
    async with session_maker() as session:
        pass