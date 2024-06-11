import pytest
import pandas as pd

CIFAR100_DATA_PATH = "data/cifar-100-python.tar.gz.dvc"

@pytest.fixture
def cifar100_data():
    data = pd.read_csv(CIFAR100_DATA_PATH)
    return data

def test_data_not_empty(cifar100_data):
    assert not cifar100_data.empty
