import os
from tests.test_topup_flow import TestTopUpFlow
from locust import HttpUser, task, between
from adapter.api.service_client import ServiceClient
from infrastructure.datasource.data_factory import get_datasource
from tests.test_update_data_flow import TestUpdateDataFlow
from config.settings import settings
import infrastructure.monitoring.influx_client

datasource = get_datasource()

SCENARIOS = os.getenv("SCENARIOS","").split(",")

SCENARIO_REGISTRY = {
    "update" : TestUpdateDataFlow,
    "topup": TestTopUpFlow
}

class LoadTestUser(HttpUser):
    host = settings.BASE_URL
    wait_time = between(1, 3)

    # init
    def on_start(self):
        """
        Wrap the Locust HTTP client with a ServiceClient and assign it to the instance.
        
        This replaces the raw `self.client` with a `ServiceClient` wrapper that provides the test's higher-level request utilities.
        """
        self.client = ServiceClient(self.client)

    
    @task
    def run_test_scenario(self):
        """
        Execute configured test scenarios in sequence.
        
        For each name in SCENARIOS that maps to a class in SCENARIO_REGISTRY, obtain data from the datasource, instantiate the scenario with self.client and the data, and invoke its run method.
        """
        for scenario_name in SCENARIOS:
            scenario_class = SCENARIO_REGISTRY.get(scenario_name)

            if not scenario_class:
                continue

            data = datasource.get_data()

            scenario = scenario_class(self.client,data)
            scenario.run()

    # @task
    # def flow_update_data(self):
    #     data = datasource.get_data()

    #     if not data:
    #         return
    #     client = ServiceClient(self.client)

    #     test = TestUpdateDataFlow(client, data)
    #     test.run()