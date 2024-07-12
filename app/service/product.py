from app.schemas import ProductCreate, ProductImageCreate
from app.util import IUnitOfWork, BaseService

class ProductService(BaseService):

    repository = 'product'

    