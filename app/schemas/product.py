from .base import BaseRead, BaseCreate, BaseUpdate
from typing import Optional

class ProductRead(BaseRead):
    name: str
    description: str
    price: float
    category_id: int


class ProductImageRead(BaseRead):
    product_id: int
    image_url: str


class ProductCreate(BaseCreate):
    name: str
    description: str
    price: float
    category_id: int

class ProductImageCreate(BaseCreate):
    product_id: int
    image_url: str

class ProductUpdate(BaseUpdate):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category_id: Optional[int] = None

class ProductImageUpdate(BaseUpdate):
    product_id: Optional[int] = None
    image_url: Optional[str] = None
