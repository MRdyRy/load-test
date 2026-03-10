class TestUpdateDataFlow:
    def __init__(self, client, data):
        self.client = client
        self.data = data
    
    def run(self):
        password = self.data.get("password") or self.data.get("pasword")
        username = self.data.get("username")
        data_id = self.data.get("id")
        
        if not username or not data_id:
            return

        self.client.login(username, password)
        
        self.client.data.inquiry_food(data_id)
        
        # Ensure payload exists
        payload = self.data.get("payload", {})
        self.client.data.update_food(data_id, payload)
        
        self.client.logout()