import pytest

from src.phone import Phone


def test_calculate_total_price(get_phone):
    phone = get_phone

    assert phone.calculate_total_price() == 15000 * 21


def test_apply_discount(get_phone):
    phone = get_phone
    Phone.pay_rate = 1
    phone.apply_discount()

    assert phone.price == 15000

    Phone.pay_rate = 0.85
    phone.apply_discount()

    assert phone.price == 15000 * Phone.pay_rate


def test_string_to_number():
    assert Phone.string_to_number('5') == 5
    assert Phone.string_to_number('5.0') == 5
    assert Phone.string_to_number('5.5') == 5


def test_repr(get_phone):
    assert repr(get_phone) == "Phone('Смартфон', 15000, 21, 3)"


def test_str(get_phone):
    assert str(get_phone) == 'Смартфон'


def test_add(get_phone):
    assert get_phone + get_phone == get_phone.quantity + get_phone.quantity

    with pytest.raises(TypeError):
        get_phone + 50


def test_sim(get_phone):
    assert get_phone.number_of_sim == 3

    get_phone.number_of_sim = 5

    assert  get_phone.number_of_sim == 5

    with pytest.raises(ValueError):
        get_phone.number_of_sim = 0
