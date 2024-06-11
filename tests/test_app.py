import unittest
import requests

class TestApp(unittest.TestCase):
    def test_homepage(self):
        response = requests.get("http://localhost:8501")
        self.assertEqual(response.status_code, 200)

    def test_prediction(self):
        url = "http://localhost:8501/predict"
        image_path = 'tests/sample_image.jpg'
        with open(image_path, 'rb') as img:
            files = {'file': img}
            response = requests.post(url, files=files)
            self.assertEqual(response.status_code, 200)
            self.assertIn("prediction", response.json())
