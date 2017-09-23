class Bot(object):

    def __init__(self, slack_client):
        self.slack_client = slack_client

    def handle_event(self, event):
        self.slack_client.api_call(
            "chat.postMessage",
            channel="#general",
            text="I just got some message"
        )
