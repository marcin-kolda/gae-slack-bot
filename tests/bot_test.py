import unittest

from src.bot import Bot
from src.event import Event
from mock import patch, Mock


class BotTest(unittest.TestCase):
    @patch.object(Bot, "get_bot_id", return_value="my_bot_id")
    def setUp(self, get_bot_id=None):  # pylint: disable=W0221
        self.slack_client = Mock()
        self.bot = Bot(self.slack_client)

    def test_ignore_own_messages(self):
        # given
        event = Event({'api_app_id': 'api_app_id',
                       'authed_users': ['U75KAHN4T'],
                       "event": {"text": "<@U75KAHN4T> hey",
                                 "username": "GCP Bot",
                                 "bot_id": "my_bot_id",
                                 "type": "message",
                                 "subtype": "bot_message",
                                 "ts": "1506206439.000011",
                                 "channel": "D75RLTNNR",
                                 "event_ts": "1506206439.000011"},
                       'event_id': 'event_id',
                       'event_time': 1506187774,
                       'team_id': 'team_id',
                       'token': 'token',
                       'type': 'event_callback'})
        # when
        self.bot.handle_event(event)

        # then
        self.slack_client.api_call.assert_not_called()

    def test_reply_successfully(self):
        # given
        event = Event({'api_app_id': 'api_app_id',
                       'authed_users': ['U75KAHN4T'],
                       'event': {'channel': 'D75RLTNNR',
                                 'event_ts': '1506187774.000063',
                                 'text': 'direct message on pric',
                                 'ts': '1506187774.000063',
                                 'type': 'message',
                                 'user': 'not_bot_id'},
                       'event_id': 'event_id',
                       'event_time': 1506187774,
                       'team_id': 'team_id',
                       'token': 'token',
                       'type': 'event_callback'})
        # when
        self.bot.handle_event(event)

        # then
        self.slack_client.api_call.assert_called_once()
