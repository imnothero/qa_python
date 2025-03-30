import pytest
from main import BooksCollector

# Фикстура для создания нового объекта перед каждым тестом
@pytest.fixture
def collector():
    return BooksCollector()