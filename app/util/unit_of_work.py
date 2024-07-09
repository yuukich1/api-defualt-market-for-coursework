from abc import ABC, abstractmethod
from typing import Type
from app.models import db
import app.repositories as rep

class IUnitOfWork(ABC):

    category: Type[rep.CategoryRepository]
    order: Type[rep.OrderRepository]
    order_detail: Type[rep.OrderDetailRepository]
    product: Type[rep.ProductRepository]
    product_image: Type[rep.ProductImageRepository]
    user: Type[rep.UserRepository]
    report: Type[rep.ReportRepository]

    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError

    @abstractmethod
    async def commit(self):
        raise NotImplementedError

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError


class UnitOfWork:


    def __init__(self):
        self.session_factory = db


    async def __aenter__(self):
        self.session = self.session_factory()
        self.category = rep.CategoryRepository(self.session)
        self.order = rep.OrderRepository(self.session)
        self.order_detail = rep.OrderDetailRepository(self.session)
        self.product = rep.ProductRepository(self.session)
        self.product_image = rep.ProductImageRepository(self.session)
        self.user = rep.UserRepository(self.session)
        self.report = rep.ReportRepository(self.session)
        return self


    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.rolllback()
        await self.session.close()


    async def commit(self):
        await self.session.commit()


    async def rolllback(self):
        await self.session.rollback()



