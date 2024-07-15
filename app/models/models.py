from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from sqlalchemy import ForeignKey
from datetime import datetime
import app.schemas as scheme

class Base(DeclarativeBase):
    ...

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(unique=True)
    username: Mapped[str]
    password: Mapped[str]
    profile_picture: Mapped[str]
    role: Mapped[str]
    verify: Mapped[bool] = mapped_column(default=False)


    def to_read_model(self):
        return scheme.UserRead(
            id=self.id,
            email=self.email,
            username=self.username,
            role=self.role,
            profile_picture=self.profile_picture
        )


class Category(Base):
    __tablename__ = 'categories'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]


    def to_read_model(self):
        return scheme.CategoryRead(
            id=self.id,
            name=self.name,
            description=self.description
        )

class Product(Base):
    __tablename__ = 'products'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]
    price: Mapped[float]
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    product_image = relationship('ProductImage', cascade='all, delete')


    def to_read_model(self):
        return scheme.ProductRead(
            id=self.id,
            name=self.name,
            description=self.description,
            price=self.price,
            category_id=self.category_id
        )



class ProductImage(Base):
    __tablename__ = 'product_images'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    image_url: Mapped[str]


    def to_read_model(self):
        return scheme.ProductImageRead(
            id=self.id,
            product_id=self.product_id,
            image_url=self.image_url
        )




   
class Order(Base):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    order_detail_id: Mapped[int] = mapped_column(ForeignKey('order_details.id'))
    status: Mapped[str]
    order_date: Mapped[datetime]
    order_detail = relationship('OrderDetail', cascade='all, delete')


    def to_read_model(self):
        return scheme.OrderRead(
            id=self.id,
            user_id=self.user_id,
            order_detail_id=self.order_detail_id,
            status=self.status,
            order_date=self.order_date
        )



class OrderDetail(Base):
    __tablename__ = 'order_details'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    quantity: Mapped[int]


    def to_read_model(self):
        return scheme.OrderDetailRead(
            id=self.id,
            product_id=self.product_id,
            quantity=self.quantity
        )



class Report(Base):
    __tablename__ ='reports'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    message: Mapped[str]


    def to_read_model(self):
        return scheme.ReportRead(
            id=self.id,
            user_id=self.user_id,
            product_id=self.product_id,
            message=self.message
        )





































































































