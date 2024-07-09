from .base import BaseRead
from datetime import datetime

class OrderRead(BaseRead):
    user_id: int
    order_detail_id: int
    status: str
    order_date: datetime


class OrderDetailRead(BaseRead):
    product_id: int
    quantity: int