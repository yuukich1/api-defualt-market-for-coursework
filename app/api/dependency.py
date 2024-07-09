from fastapi import Depends
from typing import Annotated
from app.util.unit_of_work import IUnitOfWork, UnitOfWork

UOWDdep = Annotated[IUnitOfWork, Depends(UnitOfWork)]