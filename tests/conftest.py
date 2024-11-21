import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def get_item():
    return Item("Ноутбук", 15000, 21)

@pytest.fixture
def get_phone():
    return Phone("Смартфон", 15000, 21, 3)
