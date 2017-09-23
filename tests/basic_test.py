import unittest
import json
from src import main


class BasicTest(unittest.TestCase):
    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def test_verification_handshake(self):
        # given
        challenge = "3eZbrw1aBm2rZgRNFdxV"
        request = {
            "token": "Jhj5dZrVaK7ZwHHjRyZWjbDl",
            "challenge": challenge,
            "type": "url_verification"
        }
        # when
        response = self.app.post('/slack/event',
                                 data=json.dumps(request),
                                 content_type='application/json')

        # then
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['challenge'], challenge)
