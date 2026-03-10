from locust import HttpUser, task, between
from adapter.api.service_client import ServiceClient
from infrastructure.datasource.data_factory import get_datasource
from tests.test_update_data_flow import TestUpdateDataFlow
from config.settings import settings

datasource = get_datasource()

class LoadTestUser(HttpUser):
    host = settings.BASE_URL
    wait_time = between(1, 3)

    @task
    def flow_update_data(self):
        data = datasource.get_data()

        if not data:
            return
        client = ServiceClient(self.client)

        test = TestUpdateDataFlow(client, data)
        test.run()