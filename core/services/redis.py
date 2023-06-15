import aioredis
from core.common import settings


redis_service = aioredis.from_url(
    url=f"redis://{settings.REDIS_HOST}",
    password=settings.REDIS_PASSWORD,
    port=settings.REDIS_PORT,
    decode_responses=True,
)

