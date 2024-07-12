from pydantic import BaseModel

class BaseRead(BaseModel):
    id: int

class BaseCreate(BaseModel):
    pass


class BaseUpdate(BaseModel):
    pass