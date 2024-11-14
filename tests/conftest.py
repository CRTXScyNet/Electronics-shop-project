import pytest

from src.item import Item


@pytest.fixture
def get_item():
    return Item("Ноутбук", 15000, 21)
