## Run

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirement.txt
```

```bash
python -m locust -f runner/locustfile.py
```

```bash
python -m locust -f runner/locustfile.py --headless -u 10 -r 2 -t 1m --host http://localhost:8000
```

HLD :
client -> load-test-service -> influxdb

monitoring:
grafana -> influxdb

running specific test :
<img src="https://github.com/MRdyRy/load-test/blob/f/refactor/configurable/assets/running-locust.png"/>

sample dashboard :
<img src="https://github.com/MRdyRy/load-test/blob/f/refactor/configurable/assets/sample%20dashboard.png"/>
