class Event(object):
    def __init__(self, json_event):
        self.__json_event = json_event

    def is_private_message(self):
        return self.__json_event['event']['channel'].startswith('D')

    @property
    def user_id(self):
        return self.__json_event['event'].get('user', None)

    @property
    def text(self):
        return self.__json_event['event']['text']

    @property
    def type(self):
        return self.__json_event['event']['type']

    @property
    def channel(self):
        return self.__json_event['event']['channel']
