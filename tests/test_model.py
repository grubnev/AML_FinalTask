import pytest
import torch
from torchvision.models import resnet50
from torchvision.transforms import Compose, ToTensor, Resize
from PIL import Image

# Путь к вашим весам модели
RESNET50_CIFAR10_PATH = "models/resnet50_cifar10.pth"
RESNET50_CIFAR100_PATH = "models/resnet50_cifar100.pth"

@pytest.fixture
def model():
    model = resnet50(pretrained=False)
    return model

@pytest.fixture
def cifar10_weights():
    weights = torch.load(RESNET50_CIFAR10_PATH)
    return weights

@pytest.fixture
def cifar100_weights():
    weights = torch.load(RESNET50_CIFAR100_PATH)
    return weights

def test_model_cifar10_loaded_correctly(model, cifar10_weights):
    assert isinstance(model, torch.nn.Module)
    model.load_state_dict(cifar10_weights)
    assert isinstance(model, torch.nn.Module)

def test_model_cifar100_loaded_correctly(model, cifar100_weights):
    assert isinstance(model, torch.nn.Module)
    model.load_state_dict(cifar100_weights)
    assert isinstance(model, torch.nn.Module)
