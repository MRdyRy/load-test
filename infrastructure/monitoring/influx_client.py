from influxdb_client import InfluxDBClient, Point
from config.settings import settings

class InfluxClient:
    def __init__(self):
        self.client = InfluxDBClient(
            url=settings.INFLUX_URL,
            token=settings.INFLUX_TOKEN,
            org=settings.INFLUX_ORG,
            bucket=settings.INFLUX_BUCKET
        )

        self.write_api = self.client.write_api()

    def write_latency(self, endpoint, latency):
        point = Point("api_metrics") \
            .tag("endpoint", endpoint) \
            .field("latency", latency)

        self.write_api.write(
            bucket=settings.INFLUX_BUCKET, 
            org=settings.INFLUX_ORG, 
            record=point
            )