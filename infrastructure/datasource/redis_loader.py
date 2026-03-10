import redis
import json
from config.settings import settings
import logging
from typing import Any, cast

logger = logging.getLogger(__name__)
class RedisLoader:
    def __init__(self):
        self.client = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            decode_responses=True
        )
        # Ping the server to verify the connection
        self.client.ping()

    def get_data(self):
        data = self.client.get("user_test")
        if data:
            logger.info("Data retrieved from Redis: %s", data)
            # data is typed as ResponseT (which includes Awaitable[Any]) by some type checkers
            # but in this synchronous client, it returns str/bytes/None.
            return json.loads(cast(Any, data))
        logger.warning("Data not found in Redis")
        return None