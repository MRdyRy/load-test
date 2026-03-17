from influxdb_client.client.write.point import Point
from locust import events
from infrastructure.monitoring.influx_client import listener
from config.settings import settings
import time


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("[EVENT] -- Test started")

@events.spawning_complete.add_listener
def on_spawning_complete(user_count, **kwargs):
    print("[EVENT] -- Spawning complete")
    point = Point("runtime_metrics") \
        .tag("event", "spawning_complete") \
        .field("user_count", user_count) \
        .time(time.time_ns())

    listener.write_api.write(
        bucket=settings.INFLUX_BUCKET, 
        org=settings.INFLUX_ORG, 
        record=point)