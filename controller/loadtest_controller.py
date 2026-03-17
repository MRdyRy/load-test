from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator.test_runner import run_load_test
import logging

logger = logging.getLogger(__name__)

app = FastAPI()

class LoadTestRequest(BaseModel):
    scenario: str
    users: int = 10
    spawn_rate: int = 2
    duration: str = "1m"

@app.post("/loadtest/run")
def run_test(request: LoadTestRequest):
    """
    Trigger a load test using parameters from a LoadTestRequest and return a start acknowledgement.
    
    Parameters:
        request (LoadTestRequest): Load test configuration containing:
            - scenario: identifier or path of the test scenario
            - users: number of concurrent users to simulate
            - spawn_rate: rate at which users are spawned
            - duration: duration of the test (e.g., "1m")
    
    Returns:
        dict: A summary object with keys:
            - "status": "started"
            - "scenario": the scenario from the request
            - "users": the user count from the request
    """
    logger.info("running load test for request %s", request)
    print("running load test for request %s", request)
    run_load_test(
        scenario=request.scenario,
        users=request.users,
        spawn_rate=request.spawn_rate,
        duration=request.duration
    )

    return {
        "status": "started",
        "scenario": request.scenario,
        "users": request.users
    }