from prometheus_client import start_http_server, Counter, Histogram, Gauge
import time
from flask import Flask

app = Flask(__name__)

REQUEST_COUNTER = Counter('app_requests_total', 'Total app HTTP requests')
RESPONSE_TIME = Histogram('app_response_time_seconds', 'Response time in seconds')
ACTIVE_REQUESTS = Gauge('app_active_requests', 'Number of active requests')

@app.route('/')
def hello_world():
    start_time = time.time()
    ACTIVE_REQUESTS.inc()  # Increase gauge by 1
    REQUEST_COUNTER.inc()  # Increment the counter
    response = 'Hello, World!'
    RESPONSE_TIME.observe(time.time() - start_time)  # Observe response time
    ACTIVE_REQUESTS.dec()  # Decrease gauge by 1 after response
    return response

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)
