from fastapi import APIRouter, HTTPException
from app.schemas import ProductRead, ProductCreate, ProductUpdate
from app.api.dependency import UOWDdep
from app.service import ProductService
from fastapi_cache.decorator import cache

router = APIRouter(prefix="/products", tags=["products"])

@router.post('/', response_model=ProductRead)
async def create_product(product: ProductCreate, uow: UOWDdep):
    product = await ProductService().create(product, uow)
    if not product:
        raise HTTPException(status_code=400, detail="Product not created")
    return product

@router.get('/', response_model=list[ProductRead])
@cache(expire=30)
async def get_all_products(uow: UOWDdep):
    product = await ProductService().read_all(uow)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.get('/{id}', response_model=ProductRead)
@cache(expire=5)
async def get_product(id: int, uow: UOWDdep):
    product = await ProductService().read_one(uow, id=id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put('/{id}', response_model=ProductRead)
async def update_product(id: int, product: ProductUpdate, uow: UOWDdep):
    product = await ProductService().update(id, product, uow)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.delete('/{id}', response_model=dict)
async def delete_product(id: int, uow: UOWDdep):
    product = await ProductService().delete(id, uow)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}

