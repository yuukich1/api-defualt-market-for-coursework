from .base import BaseRead, BaseModel


class ProductRead(BaseRead):
    name: str
    description: str
    price: float
    category_id: int


class ProductImageRead(BaseRead):
    product_id: int
    image_url: str


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    category_id: int

class ProductImageCreate(BaseModel):
    product_id: int
    image_url: str





