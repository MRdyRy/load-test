import time
from influxdb_client.client.influxdb_client import InfluxDBClient
from influxdb_client.client.write.point import Point
from config.settings import settings
from locust import events

class InfluxClient:
    def __init__(self):
        """
        Initialize the InfluxClient by configuring an InfluxDB client and write API, then send a test point to the configured bucket.
        
        This method:
        - Creates an InfluxDBClient using connection settings from the global `settings` module.
        - Retrieves a write API from the client for writing points.
        - Writes a single test Point ("test" with field "value" = 1) to the configured bucket to verify connectivity.
        """
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
        """
        Record an HTTP request metric in InfluxDB using the provided request details.
        
        Parameters:
            request_type (str): HTTP method or request type (e.g., "GET", "POST").
            endpoint (str): The endpoint or route name for the request.
            status (str): Request outcome label (e.g., "success", "error", or an HTTP status code).
            response_time (float): Measured response time for the request (milliseconds).
            response_length (int): Size of the response payload in bytes.
        """
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
    """
    Handle a Locust request event by determining outcome and forwarding metrics to the monitoring client.
    
    Parameters:
        request_type (str): HTTP method or request category (e.g., "GET", "POST").
        name (str): The endpoint or request name.
        response_time (float|int): Request duration in milliseconds.
        response_length (int): Size of the response in bytes.
        exception (Exception|None): Exception instance if the request failed, otherwise None.
    
    Behavior:
        Prints a brief event line, computes a status of "error" when `exception` is present or "success" otherwise, and forwards the request metrics to the configured InfluxDB listener.
    """
    print(f"[EVENT] -- {request_type} {name} {response_time}ms")
    if exception:
        status = "error"
    else:
        status = "success"
    listener.on_request(request_type, name, status, response_time, response_length)