import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")
    INFLUX_URL = os.getenv("INFLUX_URL", "http://localhost:8086")
    INFLUX_TOKEN = os.getenv("INFLUX_TOKEN", "token")
    INFLUX_ORG = os.getenv("INFLUX_ORG", "ryan")
    INFLUX_BUCKET = os.getenv("INFLUX_BUCKET", "performance")

    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
    REDIS_DB = int(os.getenv("REDIS_DB", "0"))
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "password")


    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = int(os.getenv("DB_PORT", "5432"))
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
    DB_NAME = os.getenv("DB_NAME", "loadtest")

    DATA_SOURCE=os.getenv("DATA_SOURCE", "redis")

    BASE_URL_FOOD_SERVICE = os.getenv("BASE_URL_FOOD_SERVICE", "http://localhost:8001")

    BASE_URL_LOGIN_SERVICE = os.getenv("BASE_URL_LOGIN_SERVICE", "http://localhost:8002")

settings = Settings()