from flask import Flask, request, jsonify
import redis
import time

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/track', methods=['POST'])
def track_event():
    data = request.get_json()
    event_type = data.get('event_type')
    user_id = data.get('user_id')
    
    if not event_type or not user_id:
        return jsonify({'error': 'event_type and user_id are required'}), 400
    
    # Store the event with a timestamp
    event_key = f"event:{event_type}:{int(time.time())}"
    r.set(event_key, user_id)
    r.expire(event_key, 3600)  # Keep the event for 1 hour
    
    # Increment counters for real-time analytics
    r.incr(f"count:{event_type}")
    r.incr(f"user:{user_id}:{event_type}")
    
    return jsonify({'status': 'event tracked'})

if __name__ == '__main__':
    app.run(port=5001)
