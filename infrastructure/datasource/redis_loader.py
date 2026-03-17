import redis
import json
from config.settings import settings
import logging
from typing import Any, cast

logger = logging.getLogger(__name__)
class RedisLoader:
    def __init__(self):
        """
        Initialize the RedisLoader by creating a Redis client configured from application settings and verifying connectivity.
        
        Creates a redis.Redis client using REDIS_HOST, REDIS_PORT, REDIS_DB, and sets responses to be decoded to strings. Immediately pings the Redis server to confirm the connection.
        """
        self.client = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            decode_responses=True
        )
        # Ping the server to verify the connection
        self.client.ping()

    def get_data(self):
        """
        Retrieve the JSON value stored at the Redis key "user_test" and return it as a Python object.
        
        If the key exists, parse the stored JSON string and return the resulting Python object (e.g., dict, list, or primitive). If the key does not exist, return None.
        
        Returns:
            The parsed JSON value if present, otherwise None.
        """
        data = self.client.get("user_test")
        if data:
            logger.info("Data retrieved from Redis: %s", data)
            # data is typed as ResponseT (which includes Awaitable[Any]) by some type checkers
            # but in this synchronous client, it returns str/bytes/None.
            return json.loads(cast(Any, data))
        logger.warning("Data not found in Redis")
        return None