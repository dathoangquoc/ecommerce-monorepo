"""
Dependency function for FastAPI or context-managed session usage
"""

from .engine import session_maker


async def get_db():
    async with session_maker() as session:
        yield session