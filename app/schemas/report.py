from .base import BaseRead

class ReportRead(BaseRead):
    user_id: int
    product_id: int
    message: str