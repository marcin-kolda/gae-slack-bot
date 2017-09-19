import logging
import pprint

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/slack/event', methods=['POST'])
def slack_event():
    json = request.get_json()
    logging.debug(pprint.pformat(json))
    # add token verification
    if 'challenge' in json:
        return jsonify({
            'challenge': json['challenge']
        })


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
