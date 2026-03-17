import subprocess
import os

def run_load_test(scenario, users, spawn_rate, duration):
    """
    Start a Locust headless load test in a background process using the provided scenario and load parameters.
    
    Sets the environment variable `SCENARIOS` to the given `scenario` and launches a Locust runner configured with the specified number of users, spawn rate, and test duration. The test targets http://localhost:8000 and runs without blocking the caller; the function does not return the spawned process or wait for completion.
    
    Parameters:
        scenario (str): Scenario identifier placed into the `SCENARIOS` environment variable for the Locust runner.
        users (int): Total number of simulated users to run.
        spawn_rate (int | float): Rate at which users are spawned (users per second).
        duration (str): Test duration string accepted by Locust (for example, "1m", "30s", or "1h").
    """
    env = os.environ.copy()
    env["SCENARIOS"] = scenario
    print("running load test for scenario %s", scenario)
    print("running load test for users %s", users)
    print("running load test for spawn_rate %s", spawn_rate)
    print("running load test for duration %s", duration)
    print("running load test for env %s", env)
    command = [
        "locust",
        "-f",
        "runner/locustfile.py",
        "--headless",
        "-u",
        str(users),
        "-r",
        str(spawn_rate),
        "-t",
        duration,
        "--host",
        "http://localhost:8000"
    ]

    subprocess.Popen(command, env=env)