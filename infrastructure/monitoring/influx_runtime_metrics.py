from influxdb_client.client.write.point import Point
from locust import events
from infrastructure.monitoring.influx_client import listener
from config.settings import settings
import time


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    """
    Log that the Locust test has started by printing an informational message.
    
    Parameters:
        environment (locust.env.Environment): The Locust test environment provided by the event.
        **kwargs: Additional event-specific keyword arguments (ignored).
    """
    print("[EVENT] -- Test started")

@events.spawning_complete.add_listener
def on_spawning_complete(user_count, **kwargs):
    """
    Record Locust spawning completion to InfluxDB and log a console message.
    
    Parameters:
        user_count (int): Number of users that were spawned.
    
    Description:
        Prints a spawning-complete event to standard output, creates an InfluxDB Point named "runtime_metrics"
        with tag `event="spawning_complete"`, a `user_count` field set to the provided value, and a timestamp
        set to the current time in nanoseconds. The point is written to the configured InfluxDB bucket and org.
    """
    print("[EVENT] -- Spawning complete")
    point = Point("runtime_metrics") \
        .tag("event", "spawning_complete") \
        .field("user_count", user_count) \
        .time(time.time_ns())

    listener.write_api.write(
        bucket=settings.INFLUX_BUCKET, 
        org=settings.INFLUX_ORG, 
        record=point)