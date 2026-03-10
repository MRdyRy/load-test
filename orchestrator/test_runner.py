import subprocess
import os

def run_load_test(scenario, users, spawn_rate, duration):
    env = os.environ.copy()
    env["SCENARIOS"] = scenario

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