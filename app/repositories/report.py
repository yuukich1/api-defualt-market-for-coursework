from app.models import Report
from app.util.repository import SQLAlchemyRepository

class ReportRepository(SQLAlchemyRepository):

    model = Report