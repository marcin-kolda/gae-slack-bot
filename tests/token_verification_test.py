import unittest
import json
from src import main


class TokenVerificationTest(unittest.TestCase):
    def setUp(self):
        main.app.testing = True
        main.verification_token = "correct_token"
        self.app = main.app.test_client()

    def test_should_verify_token_successfully(self):
        # given
        request = {
            "token": "correct_token",
            "challenge": "3eZbrw1aBm2rZgRNFdxV",
            "type": "url_verification"
        }
        # when
        response = self.app.post('/slack/event',
                                 data=json.dumps(request),
                                 content_type='application/json')

        # then
        self.assertEqual(response.status_code, 200)

    def test_should_fail_on_wrong_token(self):
        # given
        request = {
            "token": "wrong_token",
            "challenge": "123",
            "type": "url_verification"
        }
        # when
        response = self.app.post('/slack/event',
                                 data=json.dumps(request),
                                 content_type='application/json')

        # then
        self.assertEqual(response.status_code, 403)

    def test_should_fail_on_no_token(self):
        # given
        request = {}
        # when
        response = self.app.post('/slack/event',
                                 data=json.dumps(request),
                                 content_type='application/json')

        # then
        self.assertEqual(response.status_code, 401)
