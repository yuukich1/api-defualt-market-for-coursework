from fastapi import FastAPI
import app.api as router
from app.util import cache_init


app = FastAPI()

app.include_router(router.category_router)
app.include_router(router.product_router)


app.add_event_handler("startup", cache_init)