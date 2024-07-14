from .base import BaseRead, BaseCreate, BaseUpdate
from typing import Optional, List

class ProductRead(BaseRead):
    name: str
    description: str
    price: float
    category_id: int


class ProductCreate(BaseCreate):
    name: str
    description: str
    price: float
    category_id: int


class ProductUpdate(BaseUpdate):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category_id: Optional[int] = None


class ProductImageRead(BaseRead):
    product_id: int
    image_url: str


class ProductImageUpdate(BaseUpdate):
    product_id: Optional[int] = None
    image_url: Optional[str] = None

class ProductWithImagesRead(ProductRead):
    name: str
    description: str
    price: float
    category_id: int
    images: List[ProductImageRead]