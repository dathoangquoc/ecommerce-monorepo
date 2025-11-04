"""
Initializes the database engine and session factory.

Dependency function for FastAPI or context-managed session usage.
"""

from sqlalchemy import create_engine,  text

from .config import DBSettings

engine = create_engine(
    url=f"postgresql://{DBSettings.USERNAME}:{DBSettings.PASSWORD}@{DBSettings.HOST}:{DBSettings.PORT}/{DBSettings.DB_NAME}"
)

