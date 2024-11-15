"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price(get_item):
    item = get_item

    assert item.calculate_total_price() == 15000 * 21


def test_apply_discount(get_item):
    item = get_item
    Item.pay_rate = 1
    item.apply_discount()

    assert item.price == 15000

    Item.pay_rate = 0.85
    item.apply_discount()

    assert item.price == 15000 * Item.pay_rate
