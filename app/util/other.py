from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
import os

async def cache_init():
    redis = aioredis.from_url('redis://', decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix='fastapi_cache')


async def remove_null_values_from_dict(data: dict) -> dict:
    return {k: v for k, v in data.items() if v is not None}


async def save_file(file, upload_dir):
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    file_path = os.path.join(upload_dir, file.filename)
    with open(file_path, 'wb') as f:
        f.write(file.file.read())

    return file_path