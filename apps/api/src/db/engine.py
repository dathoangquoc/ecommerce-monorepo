"""
Initializes the database engine and session factory.
"""

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from .config import DBSettings


engine = create_async_engine(url=f"postgresql://{DBSettings.USERNAME}:{DBSettings.PASSWORD}@{DBSettings.HOST}:{DBSettings.PORT}/{DBSettings.DB_NAME}")
session_maker = async_sessionmaker(engine, expire_on_commit=False)