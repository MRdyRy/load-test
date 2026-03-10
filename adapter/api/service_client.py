from .base_client import BaseClient
from .auth_api import AuthAPI
from .data_api import DataAPI

class ServiceClient(BaseClient):
    def __init__(self, http_client):
        super().__init__(http_client)
        self.auth = AuthAPI(self)
        self.data = DataAPI(self)

    def login(self, username, password):
        return self.auth.login(username, password)

    def logout(self):
        res = self.auth.logout()
        self.token = None # Clear token on logout
        return res
