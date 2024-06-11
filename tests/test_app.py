import unittest
import requests

class TestApp(unittest.TestCase):
    def test_homepage(self):
        response = requests.get("http://localhost:8501")
        self.assertEqual(response.status_code, 200)
