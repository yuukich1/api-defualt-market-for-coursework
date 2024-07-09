from app.models import Order, OrderDetail
from app.util.repository import SQLAlchemyRepository

class OrderRepository(SQLAlchemyRepository):

    model = Order

class OrderDetailRepository(SQLAlchemyRepository):

    model = OrderDetail