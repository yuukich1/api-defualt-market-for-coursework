from .base import BaseRead, BaseCreate, BaseUpdate
from pydantic import EmailStr

class UserRead(BaseRead):
    email: EmailStr
    username: str
    password: str
    profile_picture: str
    role: str

class UserCreate(BaseCreate):
    email: EmailStr
    username: str
    password: str
    