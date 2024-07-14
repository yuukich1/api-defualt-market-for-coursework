from app.schemas import ProductCreate
from app.util import IUnitOfWork, BaseService, save_file
from fastapi import UploadFile
from app.config import IMAGE_DIRECTOR_URL


class ProductService(BaseService):

    repository = 'product'

class ProductImageService(BaseService):

    repository = 'product_image'

    
    async def create(self, product_id: int, image: UploadFile, uow: IUnitOfWork):
        async with uow: 
            image_url = await save_file(file=image, upload_dir=IMAGE_DIRECTOR_URL)
            image_data = {'product_id': product_id, 'image_url': image.filename}
            product_image = await uow.product_image.create(image_data)
            await uow.commit()
            return product_image

