import unittest
from src.nlu.nlu_setup import setup_nlu

class TestNLU(unittest.TestCase):
    def test_setup_nlu(self):
        nlu = setup_nlu()
        self.assertIsNotNone(nlu)

if __name__ == '__main__':
    unittest.main()
