from fastapi import APIRouter, HTTPException
from app.schemas import CategoryCreate, CategoryRead, CategoryUpdate
from .dependency import UOWDdep
from app.service import CategoryService
from fastapi_cache.decorator import cache

router = APIRouter(prefix="/categories", tags=["category"])


@router.post("/", response_model=CategoryRead)
async def create_category(category: CategoryCreate, uow: UOWDdep):
    category = await CategoryService().create(category, uow)
    if not category:
        raise HTTPException(status_code=400, detail="Category not created")
    return category


@router.get("/", response_model=list[CategoryRead])
@cache(expire=30)
async def get_categories(uow: UOWDdep):
    categories = await CategoryService().read_all(uow)
    if not categories:
        raise HTTPException(status_code=404, detail="No categories found")
    return categories


@router.get("/{id}", response_model=CategoryRead)
@cache(expire=5)
async def get_category(id: int, uow: UOWDdep):
    category = await CategoryService().read_one(uow, id=id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.put("/{id}", response_model=CategoryRead)
async def update_category(id: int, category: CategoryUpdate, uow: UOWDdep):
    category = await CategoryService().update(id, category, uow)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.delete("/{id}", response_model=dict)
async def delete_category(id: int, uow: UOWDdep):
    category = await CategoryService().delete(id, uow)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category deleted successfully"}
