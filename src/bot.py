import logging

class Bot(object):

    def __init__(self, slack_client):
        self.slack_client = slack_client
        self.bot_id = self.__get_bot_id()

    def __get_bot_id(self):
        bot_id = self.slack_client.api_call("auth.test")['user_id']
        logging.info("Retrieved bot_id: %s", bot_id)
        return bot_id

    def handle_event(self, event):
        pass
