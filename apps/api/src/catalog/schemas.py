"""
SQLAlchemy ORM schemas
"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from..db.base import Base


class Product(Base):
    __tablename__ = "product"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    price: Mapped[int]
    description: Mapped[str]
    count: Mapped[int]