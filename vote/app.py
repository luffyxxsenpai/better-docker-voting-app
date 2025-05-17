from flask import Flask, render_template, request, make_response, g
from redis import Redis
import os
import socket
import random
import json
import logging

# Standardized environment variables in all caps
OPTION_A = os.getenv('OPTION_A', "Cats")
OPTION_B = os.getenv('OPTION_B', "Dogs")
HOSTNAME = socket.gethostname()

# Redis connection details
REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = int(os.getenv('REDIS_PORT', '6379'))
REDIS_DB = int(os.getenv('REDIS_DB', '0'))
REDIS_SOCKET_TIMEOUT = int(os.getenv('REDIS_SOCKET_TIMEOUT', '5'))

# Debug control
ENV_INFO = os.getenv('ENV_INFO', 'no').lower() == 'yes'

app = Flask(__name__)

# Configure logging
gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.INFO)

def get_redis():
    """Establish and return a Redis connection."""
    if not hasattr(g, 'redis'):
        g.redis = Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            db=REDIS_DB,
            socket_timeout=REDIS_SOCKET_TIMEOUT
        )
    return g.redis

@app.route("/", methods=['POST', 'GET'])
def hello():
    """Handle the main voting logic."""
    voter_id = request.cookies.get('voter_id')
    if not voter_id:
        voter_id = hex(random.getrandbits(64))[2:-1]

    vote = None

    if request.method == 'POST':
        redis = get_redis()
        vote = request.form['vote']
        app.logger.info('Received vote for %s', vote)
        data = json.dumps({'voter_id': voter_id, 'vote': vote})
        redis.rpush('votes', data)

    resp = make_response(render_template(
        'index.html',
        option_a=OPTION_A,
        option_b=OPTION_B,
        hostname=HOSTNAME,
        vote=vote,
    ))
    resp.set_cookie('voter_id', voter_id)
    return resp

if __name__ == "__main__":
    if ENV_INFO:
        print(f"""
        Flask Voting App
        -----------------
        Running on: http://0.0.0.0:8080
        Environment:
          - OPTION_A: {OPTION_A}
          - OPTION_B: {OPTION_B}
          - REDIS_HOST: {REDIS_HOST}
          - REDIS_PORT: {REDIS_PORT}
          - REDIS_DB: {REDIS_DB}
          - ENV_INFO: {'yes' if ENV_INFO else 'no'}
        """)
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
