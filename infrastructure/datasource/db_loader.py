import psycopg2
import random
from config.settings import settings

class DBLoader:
    def __init__(self):
        self.connection = psycopg2.connect(
            host=settings.DB_HOST,
            port=settings.DB_PORT,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            dbname=settings.DB_NAME
        )

    def get_data(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        return random.choice(users)
