import pytest
import pandas as pd

CIFAR10_DATA_PATH = "data/cifar-10-python.tar.gz.dvc"

@pytest.fixture
def cifar10_data():
    data = pd.read_csv(CIFAR10_DATA_PATH)
    return data

def test_data_not_empty(cifar10_data):
    assert not cifar10_data.empty
