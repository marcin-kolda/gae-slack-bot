import logging


class Bot(object):
    def __init__(self, slack_client):
        self.slack_client = slack_client
        self.user_id = self.get_user_id()

    def get_user_id(self):
        response = self.slack_client.api_call("auth.test")
        if not response['ok']:
            logging.error("Unable to retrieve bot id due to %s",
                          response['error'])
        else:
            user_id = response['user_id']
            logging.info("Retrieved user_id: '%s'", user_id)
            return user_id

    def handle_event(self, event):
        if event.user_id == self.user_id:
            logging.info("Ignoring own message")
            return
        self.slack_client.api_call(
            "chat.postMessage",
            channel=event.channel,
            as_user=True,
            text=event.text
        )
