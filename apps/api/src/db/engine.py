"""
Initializes the database engine and session factory.
"""
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from .config import DBSettings


settings = DBSettings()

url = URL.create(
    drivername="postgresql+asyncpg",
    username=settings.USERNAME,
    password=settings.PASSWORD,
    host=settings.HOST,
    port=settings.PORT,
    database=settings.DB_NAME
)

engine = create_async_engine(url, echo=True)

session_maker = async_sessionmaker(engine, expire_on_commit=False)