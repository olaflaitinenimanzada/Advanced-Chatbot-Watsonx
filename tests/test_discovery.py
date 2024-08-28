import unittest
from src.discovery.discovery_setup import setup_discovery

class TestDiscovery(unittest.TestCase):
    def test_setup_discovery(self):
        discovery = setup_discovery()
        self.assertIsNotNone(discovery)

if __name__ == '__main__':
    unittest.main()
