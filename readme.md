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