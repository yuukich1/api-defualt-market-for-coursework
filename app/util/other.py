from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend


async def cache_init():
    redis = aioredis.from_url('redis://', decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix='fastapi_cache')


async def remove_null_values_from_dict(data: dict) -> dict:
    return {k: v for k, v in data.items() if v is not None}