from flask import Flask, jsonify, render_template
import redis
import time

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/metrics')
def get_metrics():
    event_types = ['page_view', 'click', 'signup']
    metrics = {event: int(r.get(f"count:{event}") or 0) for event in event_types}
    return jsonify(metrics)

if __name__ == '__main__':
    app.run(port=5002)
