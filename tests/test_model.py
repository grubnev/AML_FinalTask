import unittest
import torch
from src.model import load_model, predict

class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = load_model('models/resnet50_cifar10.pth')
        self.sample_input = torch.randn(1, 3, 32, 32)

    def test_predict(self):
        result = predict(self.model, self.sample_input)
        self.assertIsInstance(result, int)

if __name__ == '__main__':
    unittest.main()
