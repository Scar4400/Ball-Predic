from prometheus_client import Gauge, start_http_server
import time

accuracy_gauge = Gauge('model_accuracy', 'Model Accuracy')
latency_gauge = Gauge('model_latency', 'Model Latency in seconds')

def monitor_model_performance(model, test_data):
    start_http_server(8000)

    while True:
        start_time = time.time()

        # Assuming model.predict returns predictions and you compare against actuals
        predictions = model.predict(test_data['features'])
        accuracy = calculate_accuracy(predictions, test_data['labels'])

        # Record metrics
        latency_gauge.set(time.time() - start_time)
        accuracy_gauge.set(accuracy)

        time.sleep(60)  # Scrape every 60 seconds
