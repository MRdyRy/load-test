from http import HTTPStatus
from config.settings import settings
class AuthAPI:
    def __init__(self, client):
        self.client = client

    def login(self, username, password):
        r = self.client.post(
            f"{settings.BASE_URL_LOGIN_SERVICE}/auth/login", 
            json={"username": username, "password": password})
        if r.status_code == HTTPStatus.OK:
            self.client.token = r.json().get("token")
        return r


    def logout(self):
        return self.client.post(f"{settings.BASE_URL_LOGIN_SERVICE}/auth/logout")