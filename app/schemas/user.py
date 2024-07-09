from .base import BaseRead
from pydantic import EmailStr

class UserRead(BaseRead):
    email: EmailStr
    username: str
    password: str
    profile_picture: str
    role: str