"""
Database initialization, seed data, cleanup scripts.
"""

from .base import Base
from .engine import engine

def init_db():
    Base.metadata.create_all(engine)