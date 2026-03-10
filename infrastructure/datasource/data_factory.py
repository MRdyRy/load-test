from config.settings import settings
from .db_loader import DBLoader
from .redis_loader import RedisLoader

def get_datasource():
    if settings.DATA_SOURCE == "redis":
        return RedisLoader()
    elif settings.DATA_SOURCE == "db":
        return DBLoader()
    else:
        raise ValueError("Invalid datasource")