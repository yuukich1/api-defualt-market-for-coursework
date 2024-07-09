from app.models import Product, ProductImage
from app.util.repository import SQLAlchemyRepository

class ProductRepository(SQLAlchemyRepository):

    model = Product

class ProductImageRepository(SQLAlchemyRepository):

    model = ProductImage