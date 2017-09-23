import unittest

from src.event import Event


class EventTest(unittest.TestCase):

    def test_check_if_message_is_private(self):
        # given
        event = Event({'api_app_id': 'api_app_id',
                       'authed_users': ['U75KAHN4T'],
                       'event': {'channel': 'D75RLTNNR',
                                 'event_ts': '1506187774.000063',
                                 'text': 'direct message on pric',
                                 'ts': '1506187774.000063',
                                 'type': 'message',
                                 'user': 'U754USPTK'},
                       'event_id': 'event_id',
                       'event_time': 1506187774,
                       'team_id': 'team_id',
                       'token': 'token',
                       'type': 'event_callback'})
        # when
        is_private_message = event.is_private_message()

        # then
        self.assertTrue(is_private_message)

    def test_check_if_message_is_from_channel(self):
        # given
        event = Event({'api_app_id': 'api_app_id',
                       'authed_users': ['U75KAHN4T'],
                       'event': {'channel': 'C12345',
                                 'event_ts': '1506187774.000063',
                                 'text': 'direct message on pric',
                                 'ts': '1506187774.000063',
                                 'type': 'message',
                                 'user': 'U754USPTK'},
                       'event_id': 'event_id',
                       'event_time': 1506187774,
                       'team_id': 'team_id',
                       'token': 'token',
                       'type': 'event_callback'})
        # when
        is_private_message = event.is_private_message()

        # then
        self.assertFalse(is_private_message)
