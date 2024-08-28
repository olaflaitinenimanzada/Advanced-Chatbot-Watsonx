import unittest
from src.web.app import app

class TestWeb(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_chat_endpoint(self):
        response = self.app.post('/chat', json={'message': 'Hello'})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
