from flask import Flask, request, jsonify
import redis
import time
from functools import wraps

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)

# Default access rate and time window limits
RATE_LIMIT = 5  # requests
TIME_WINDOW = 60  # seconds

def rate_limit(limit=RATE_LIMIT, window=TIME_WINDOW):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user_ip = request.remote_addr
            current_time = int(time.time())

            key = f"rate_limit:{user_ip}:{request.endpoint}"
            
            # Remove outdated request timestamps
            r.zremrangebyscore(key, 0, current_time - window)

            # Check the number of requests in the current time window
            request_count = r.zcard(key)

            if request_count >= limit:
                return jsonify({'error': 'Rate limit exceeded'}), 429
            
            # Add the current request timestamp
            r.zadd(key, {current_time: current_time})

            return f(*args, **kwargs)
        return decorated_function
    return decorator

@app.route('/limited', methods=['GET'])
@rate_limit(limit=5, window=60)
def limited():
    return jsonify({'message': 'Request successful'}), 200

@app.route('/another-limited', methods=['GET'])
@rate_limit(limit=10, window=60)
def another_limited():
    return jsonify({'message': 'Another request successful'}), 200

if __name__ == '__main__':
    app.run(port=5000)
