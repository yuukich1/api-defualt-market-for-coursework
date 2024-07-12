from app.schemas import CategoryCreate, CategoryUpdate
from app.util import IUnitOfWork, remove_null_values_from_dict, BaseService


class CategoryService(BaseService):

    repository = 'category'

    


