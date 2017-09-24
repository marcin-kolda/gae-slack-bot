import logging

import settings

from flask import Flask, request, jsonify, abort

from event import Event
from bot import Bot
from slack_web_api_client import SlackWebAPIClient

app = Flask(__name__)

verification_token = settings.VERIFICATION_TOKEN

slack_client = SlackWebAPIClient(settings.BOT_ACCESS_TOKEN)
bot = Bot(slack_client)


@app.route('/')
def root():
    text = "Hello from Google App Engine! :tada:, build date: {}, git "\
           "commit: {}".format(settings.BUILD_DATE, settings.GIT_COMMIT)
    slack_client.post_message(channel='#general',
                              text=text)
    return text


@app.route('/slack/event', methods=['POST'])
def slack_event():
    logging.debug("Request payload: %s", request.data)
    event = request.get_json()
    if 'token' not in event:
        logging.error("There is no token in the JSON")
        abort(401)
    if event['token'] != verification_token:
        logging.error("Wrong token in JSON")
        abort(403)
    if 'challenge' in event:
        return jsonify({'challenge': event['challenge']})
    else:
        bot.handle_event(Event(event))
        return jsonify({})


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
