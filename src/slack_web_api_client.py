import json
import urllib
import logging

from google.appengine.api import urlfetch


class SlackWebAPIClient(object):
    def __init__(self, access_token):
        self.access_token = access_token
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    def post_message(self, channel, text, as_user=True):
        form_fields = {
            'token': self.access_token,
            'channel': channel,
            'text': text,
            'as_user': as_user
        }
        form_data = urllib.urlencode(form_fields)
        result = urlfetch.fetch(url="https://slack.com/api/chat.postMessage",
                                payload=form_data,
                                method=urlfetch.POST,
                                headers=self.headers)
        json_response = json.loads(result.content)
        if json_response['ok']:
            logging.debug("Message sent successfully")
        else:
            raise Exception("Unable to send message due to '{}' error".format(
                json_response['error']))

    def auth_test(self):
        form_fields = {
            'token': self.access_token
        }
        form_data = urllib.urlencode(form_fields)
        result = urlfetch.fetch(url="https://slack.com/api/auth.test",
                                payload=form_data,
                                method=urlfetch.POST,
                                headers=self.headers)
        return json.loads(result.content)
