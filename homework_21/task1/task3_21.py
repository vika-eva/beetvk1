import pytest
from task1_21 import FileContextManager

@pytest.fixture
def replace_file():
    return 'test.txt'

@pytest.fixture
def by_data(replace_file):
    with FileContextManager(replace_file, 'r') as f:
        data = f.read()
        return data[:11]

def test_data(by_data):
    assert by_data == "Hello World"


