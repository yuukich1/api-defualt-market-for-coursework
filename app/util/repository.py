from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select, update, delete

class AbstractRepository(ABC):

    @abstractmethod
    async def create():
        raise NotImplementedError
    
    @abstractmethod
    async def read_one():
        raise NotImplementedError
    
    @abstractmethod
    async def read_all():
        raise NotImplementedError
    
    @abstractmethod
    async def update():
        raise NotImplementedError
    
    @abstractmethod
    async def delete():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):

    model = None

    def __init__(self, session: AsyncSession) -> None:
        self.session = session


    async def create(self, data: dict):
        stmt = insert(self.model).values(**data).returning(self.model)
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none().to_read_model()
    

    async def read_one(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        return res.scalar_one().to_read_model()
    

    async def read_all(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res
    

    async def update(self, id: int, data: dict):
        stmt = update(self.model).values(**data).filter_by(id=id).returning(self.model)
        res = await self.session.execute(stmt)
        return res.scalar_one().to_read_model()
    

    async def delete(self, id: int):
        stmt = delete(self.model).filter_by(id=id)
        res = await self.session.execute(stmt)
        return res

    
