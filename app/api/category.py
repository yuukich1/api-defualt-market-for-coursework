from fastapi import APIRouter, HTTPException
from app.schemas import CategoryCreate, CategoryRead
from .dependency import UOWDdep
from app.service import CategoryService
from fastapi_cache.decorator import cache

category_router = APIRouter(prefix="/categories", tags=["category"])

@category_router.post("/", response_model=CategoryRead)
async def create_category(category: CategoryCreate, uow: UOWDdep):
    category = await CategoryService().create(category, uow)
    if not category:
        raise HTTPException(status_code=400, detail="Category already exists")
    return category


@category_router.get("/", response_model=list[CategoryRead])
@cache(expire=30)
async def get_categories(uow: UOWDdep):
    categories = await CategoryService().read_all(uow)
    if not categories:
        raise HTTPException(status_code=404, detail="No categories found")
    return categories


@category_router.get("/{id}", response_model=CategoryRead)
@cache(expire=5)
async def get_category(id: int, uow: UOWDdep):
    category = await CategoryService().read_one(uow, id=id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category




