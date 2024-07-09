from app.schemas import ProductCreate, ProductImageCreate
from app.util import IUnitOfWork

class ProductService:

    async def create(self, product: ProductCreate, uow: IUnitOfWork):
        product_dict = product.model_dump()
        async with uow:
            product = await uow.product.create(data=product_dict)
            await uow.commit()
            return product

