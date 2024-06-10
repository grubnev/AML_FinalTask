import pytest
import torchvision

def test_data_loading():
    trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=False)
    testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=False)
    assert len(trainset) == 50000
    assert len(testset) == 10000