import time
from influxdb_client.client.influxdb_client import InfluxDBClient
from influxdb_client.client.write.point import Point
from config.settings import settings
from locust import events

class InfluxClient:
    def __init__(self):
        self.client = InfluxDBClient(
            url=settings.INFLUX_URL,
            token=settings.INFLUX_TOKEN,
            org=settings.INFLUX_ORG,
            bucket=settings.INFLUX_BUCKET
        )

        print("[INIT] -- InfluxClient initialized with settings %s", settings)
        self.write_api = self.client.write_api()

        point = Point("test").field("value", 1)
        self.write_api.write(bucket=settings.INFLUX_BUCKET, record=point)

    def on_request(self, request_type, endpoint, status, response_time, response_length):
        point = Point("api_metrics") \
            .tag("method", request_type) \
            .tag("status", status) \
            .tag("endpoint", endpoint) \
            .field("response_time", response_time) \
            .field("response_length", response_length) \
            .field("count", 1) \
            .time(time.time_ns())

        print("[WRITE] -- writing point to influxdb %s", point)
        self.write_api.write(
            bucket=settings.INFLUX_BUCKET, 
            org=settings.INFLUX_ORG, 
            record=point
            )
listener = InfluxClient()

@events.request.add_listener
def _(request_type, name, response_time, response_length, exception, **kwargs):
    print(f"[EVENT] -- {request_type} {name} {response_time}ms")
    if exception:
        status = "error"
    else:
        status = "success"
    listener.on_request(request_type, name, status, response_time, response_length)