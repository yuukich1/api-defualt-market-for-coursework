from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend


async def cache_init():
    redis = aioredis.from_url('redis://', decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix='fastapi_cache')