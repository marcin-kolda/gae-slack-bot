class Event(object):

    def __init__(self, json_event):
        self.__json_event = json_event

    def is_private_message(self):
        return self.__json_event['event']['channel'].startswith('D')

    @property
    def bot_id(self):
        return self.__json_event['event'].get('bot_id', None)

    @property
    def text(self):
        return self.__json_event['event']['text']

    @property
    def channel(self):
        return self.__json_event['event']['channel']

