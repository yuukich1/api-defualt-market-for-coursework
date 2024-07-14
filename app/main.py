from fastapi import FastAPI
import app.api as router
from app.util import cache_init
from fastapi.responses import FileResponse
from app.config import IMAGE_DIRECTOR_URL
app = FastAPI()

app.include_router(router.category_router)
app.include_router(router.product_router)


app.add_event_handler("startup", cache_init)


@app.get('/image/{filename}')
async def get_image(filename: str):
    return FileResponse(f'{IMAGE_DIRECTOR_URL}/{filename}')