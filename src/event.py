class Event(object):

    def __init__(self, json_event):
        self.__json_event = json_event

    def is_private_message(self):
        return self.__json_event['event']['channel'].startswith('D')

    @property
    def user_id(self):
        return self.__json_event['event']['user']

    @property
    def text(self):
        return self.__json_event['event']['text']

    @property
    def channel(self):
        return self.__json_event['event']['channel']

