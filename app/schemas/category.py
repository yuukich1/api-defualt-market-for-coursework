from .base import BaseRead, BaseModel

class CategoryRead(BaseRead):
    name: str
    description: str

class CategoryCreate(BaseModel):
    name: str
    description: str