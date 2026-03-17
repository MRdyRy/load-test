class TestTopUpFlow:
    def __init__(self, client, data):
        """
        Initialize the TestTopUpFlow with its client and associated test data.
        
        Parameters:
            client: The client used to perform requests (e.g., a test HTTP client or API client).
            data: Test input data for the top-up flow (fixtures or payloads).
        """
        self.client = client
        self.data = data