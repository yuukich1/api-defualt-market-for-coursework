from app.models import Category
from app.util.repository import SQLAlchemyRepository

class CategoryRepository(SQLAlchemyRepository):

    model = Category