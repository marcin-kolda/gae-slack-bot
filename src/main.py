import logging
import pprint
import settings

from flask import Flask, request, jsonify, abort

app = Flask(__name__)

verification_token = settings.VERIFICATION_TOKEN


@app.route('/')
def root():
    return 'GAE Slack bot, build date: {}, git commit: {}' \
        .format(settings.BUILD_DATE, settings.GIT_COMMIT)


@app.route('/slack/event', methods=['POST'])
def slack_event():
    json = request.get_json()
    logging.debug(pprint.pformat(json))
    if 'token' not in json:
        logging.error("There is no token in the JSON")
        abort(401)
    if json['token'] != verification_token:
        logging.error("Wrong token in JSON")
        abort(403)
    if 'challenge' in json:
        return jsonify({'challenge': json['challenge']})
    else:
        return jsonify({})


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
