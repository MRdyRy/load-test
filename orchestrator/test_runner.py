import subprocess
import os

def run_load_test(scenario, users, spawn_rate, duration):
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