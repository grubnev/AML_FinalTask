import unittest
import requests

class TestApp(unittest.TestCase):
    def test_homepage(self):
        response = requests.get("http://localhost:8501")
        self.assertEqual(response.status_code, 200)

    def test_prediction(self):
        url = "http://localhost:8501/predict"
        files = {'file': open('tests/sample_image.png', 'rb')}
        response = requests.post(url, files=files)
        self.assertEqual(response.status_code, 200)
        self.assertIn("prediction", response.json())

if __name__ == '__main__':
    unittest.main()
