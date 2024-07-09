from app.schemas import CategoryCreate
from app.util import IUnitOfWork


class CategoryService:

    async def create(self, category: CategoryCreate, uow: IUnitOfWork):
        category_dict = category.model_dump()
        async with uow:
            category = await uow.category.create(category_dict)
            await uow.commit()
            return category
        

    async def read_all(self, uow: IUnitOfWork):
        async with uow:
            categories = await uow.category.read_all()
            return categories
        
        
    async def read_one(self, uow: IUnitOfWork, **filter_by):
        async with uow:
            category = await uow.category.read_one(**filter_by)
            return category


