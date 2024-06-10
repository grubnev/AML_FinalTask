import unittest
import requests
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import predict

class TestApp(unittest.TestCase):
    def test_predict(self):
        # Проверка функции predict()
        # Подготавливаем изображение, используя PIL
        image = prepare_image()
        predicted_class = predict(image)
        # Проверяем, что возвращенный класс находится в списке классов
        self.assertIn(predicted_class, classes)

    def test_app_availability(self):
        # Проверка доступности приложения по ссылке
        url = 'http://localhost:8501'  # Замените на вашу ссылку
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
