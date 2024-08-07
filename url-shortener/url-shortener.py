from flask import Flask, request, redirect, jsonify
import redis
import string
import random

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)

# Function to cache data
def cache_data(key, value, expiration=None):
    r.set(key, value)
    if expiration:
        r.expire(key, expiration)

# Function to get cached data
def get_cached_data(key):
    return r.get(key)

def generate_short_url():
    # Generates a random string of 6 characters
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    if 'url' not in data: 
        return jsonify({'error': 'No URL provided'}), 400
    long_url = data['url']
    expiry = data['expiration'] if 'expiration' in data else None
    short_url = generate_short_url()
    
    cache_data(short_url, long_url, expiry)
    return jsonify({'short_url': short_url})

@app.route('/<short_url>', methods=['GET'])
def redirect_to_long_url(short_url):
    long_url = get_cached_data(short_url)
    if long_url:
        return redirect(long_url.decode('utf-8'))
    else:
        return 'URL not found', 404

if __name__ == '__main__':
     app.run(port=5000)
