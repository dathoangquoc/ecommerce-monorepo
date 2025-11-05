"""
Pydantic models for I/O validation
"""

from typing import Optional

from pydantic import BaseModel


class ProductRead(BaseModel):
    id: int
    name: str
    price: float
    description: str
    count: int

class ProductCreate(BaseModel):
    name: str
    price: float
    description: str
    count: int

class ProductUpdate(BaseModel):
    id: int
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    count: Optional[int] = None
