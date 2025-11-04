"""
Pydantic models for I/O validation
"""

from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    price: float
    description: str
    stock_count: int


class ProductRead(BaseModel):
    id: str
    name: str
    price: float
    description: str
    stock_count: int