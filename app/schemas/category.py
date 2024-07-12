from .base import BaseRead, BaseModel, BaseCreate, BaseUpdate
from typing import Optional


class CategoryRead(BaseRead):
    name: str
    description: str

class CategoryCreate(BaseCreate):
    name: str
    description: str

class CategoryUpdate(BaseUpdate):
    name: Optional[str] = None
    description: Optional[str] = None