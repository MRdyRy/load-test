from config.settings import settings

class DataAPI:
    def __init__(self, client):
        self.client = client

    def inquiry_food(self, data_id):
        return self.client.get(f"{settings.BASE_URL_FOOD_SERVICE}/food/{data_id}")

    def update_food(self, data_id, payload):
        return self.client.put(
            f"{settings.BASE_URL_FOOD_SERVICE}/food/{data_id}", 
            json=payload
            )