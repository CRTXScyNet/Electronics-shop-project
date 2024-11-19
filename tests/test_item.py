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


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_instance_from_csv():
    Item.all.clear()
    Item.instantiate_from_csv('src\items.csv')

    assert Item.all[0].price == 100
    assert Item.all[1].price == 1000
    assert Item.all[2].price == 10

    assert Item.all[0].quantity == 1
    assert Item.all[1].quantity == 3
    assert Item.all[2].quantity == 5

def test_repr(get_item):
    assert repr(get_item) == "Item('Ноутбук', 15000, 21)"

def test_str(get_item):
    assert str(get_item) == 'Ноутбук'
