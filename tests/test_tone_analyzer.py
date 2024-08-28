import unittest
from src.tone_analyzer.tone_analyzer_setup import setup_tone_analyzer

class TestToneAnalyzer(unittest.TestCase):
    def test_setup_tone_analyzer(self):
        tone_analyzer = setup_tone_analyzer()
        self.assertIsNotNone(tone_analyzer)

if __name__ == '__main__':
    unittest.main()
