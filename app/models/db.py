from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from app.config import db_full_url
async_engine = create_async_engine(db_full_url)
async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)