import unittest

from src.bot import Bot
from src.event import Event
from mock import Mock


class BotTest(unittest.TestCase):
    def setUp(self):
        self.slack_client = Mock()
        self.bot = Bot(self.slack_client, user_id="my_user_id")

    def test_ignore_own_messages(self):
        # given
        event = Event({'api_app_id': 'api_app_id',
                       'authed_users': ['U75KAHN4T'],
                       "event": {"type": "message",
                                 "user": "my_user_id",
                                 "text": "erf",
                                 "ts": "1506208677.000067",
                                 "channel": "D75RLTNNR",
                                 "event_ts": "1506208677.000067"},
                       'event_id': 'event_id',
                       'event_time': 1506187774,
                       'team_id': 'team_id',
                       'token': 'token',
                       'type': 'event_callback'})
        # when
        self.bot.handle_event(event)

        # then
        self.slack_client.post_message.assert_not_called()

    def test_ignore_unknown_event_types(self):
        # given
        event = Event({'api_app_id': 'api_app_id',
                       'authed_users': ['U75KAHN4T'],
                       "event": {"type": "reaction_added", "user": "U754USPTK",
                                 "item": {"type": "message",
                                          "channel": "C76NQ1WQP",
                                          "ts": "1506283080.000045"},
                                 "reaction": "neutral_face",
                                 "item_user": "U75KAHN4T",
                                 "event_ts": "1506283351.000047"},
                       'event_id': 'event_id',
                       'event_time': 1506187774,
                       'team_id': 'team_id',
                       'token': 'token',
                       'type': 'event_callback'})
        # when
        self.bot.handle_event(event)

        # then
        self.slack_client.post_message.assert_not_called()

    def test_reply_successfully(self):
        # given
        event = Event({'api_app_id': 'api_app_id',
                       'authed_users': ['U75KAHN4T'],
                       'event': {'channel': 'D75RLTNNR',
                                 'event_ts': '1506187774.000063',
                                 'text': 'direct message on pric',
                                 'ts': '1506187774.000063',
                                 'type': 'message',
                                 'user': 'other_user_id'},
                       'event_id': 'event_id',
                       'event_time': 1506187774,
                       'team_id': 'team_id',
                       'token': 'token',
                       'type': 'event_callback'})
        # when
        self.bot.handle_event(event)

        # then
        self.slack_client.post_message.assert_called_once()
