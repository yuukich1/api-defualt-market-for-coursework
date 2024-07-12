from abc import ABC, abstractmethod
from app.schemas import BaseCreate, BaseUpdate
from app.util import IUnitOfWork, remove_null_values_from_dict



class AbstractService(ABC):

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
    

class BaseService(AbstractService):

    repository = None

    async def create(self, data: BaseCreate, uow: IUnitOfWork):
        data_dict = data.model_dump()
        async with uow:
            repo = getattr(uow, self.repository)
            created_obj = await repo.create(data_dict)
            await uow.commit()
            return created_obj


    async def read_all(self, uow: IUnitOfWork):
        async with uow:
            repo = getattr(uow, self.repository)
            read_obj = await repo.read_all()
            return read_obj
    
    async def read_one(self, uow: IUnitOfWork, **filter_by):
        async with uow:
            repo = getattr(uow, self.repository)
            read_obj = await repo.read_one(**filter_by)
            return read_obj
        
    
    async def update(self, id: int, data: BaseUpdate, uow: IUnitOfWork):
        data_dict = data.model_dump()
        async with uow:
            repo = getattr(uow, self.repository)
            updated_obj = await repo.update(id, data_dict)
            await uow.commit()
            return updated_obj
    
    async def delete(self, id: int, uow: IUnitOfWork):
        async with uow:
            repo = getattr(uow, self.repository)
            deleted_obj = await repo.delete(id)
            await uow.commit()
            return deleted_obj

    
    
