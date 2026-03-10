class BaseClient:
    def __init__(self, http_client):
        self.client = http_client
        self.token = None

    def get(self, url, **kwargs):
        headers = kwargs.get("headers", {})
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"    
        kwargs["headers"] = headers
        return self.client.get(url, **kwargs)

    
    def post(self, url, **kwargs):
        headers = kwargs.get("headers", {})
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"    
        kwargs["headers"] = headers
        return self.client.post(url, **kwargs)

    def put(self, url, **kwargs):
        headers = kwargs.get("headers", {})
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"    
        kwargs["headers"] = headers
        return self.client.put(url, **kwargs)