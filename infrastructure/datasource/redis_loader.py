import redis
import json
from config.settings import settings
import logging

logger = logging.getLogger(__name__)
class RedisLoader:
    def __init__(self):
        self.client = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB
        )
        # Ping the server to verify the connection
        self.client.ping()

    def get_data(self):
        data = self.client.get("user_test")
        if data:
            logger.info("Data retrieved from Redis: %s", data)
            return json.loads(data)
        logger.warning("Data not found in Redis")
        return None