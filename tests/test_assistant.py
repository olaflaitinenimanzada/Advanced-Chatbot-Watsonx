import unittest
from src.assistant.assistant_setup import setup_assistant

class TestAssistant(unittest.TestCase):
    def test_setup_assistant(self):
        assistant = setup_assistant()
        self.assertIsNotNone(assistant)

if __name__ == '__main__':
    unittest.main()
