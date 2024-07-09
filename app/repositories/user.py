from app.models import User
from app.util.repository import SQLAlchemyRepository

class UserRepository(SQLAlchemyRepository):

    model = User