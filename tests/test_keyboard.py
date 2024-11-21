import pytest

from src.keyboard import Keyboard


def test_calculate_total_price(get_keyboard):
    keyboard = get_keyboard

    assert keyboard.calculate_total_price() == 9600 * 5


def test_apply_discount(get_keyboard):
    keyboard = get_keyboard
    Keyboard.pay_rate = 1
    keyboard.apply_discount()

    assert keyboard.price == 9600

    Keyboard.pay_rate = 0.85
    keyboard.apply_discount()

    assert keyboard.price == 9600 * Keyboard.pay_rate


def test_string_to_number():
    assert Keyboard.string_to_number('5') == 5
    assert Keyboard.string_to_number('5.0') == 5
    assert Keyboard.string_to_number('5.5') == 5


def test_repr(get_keyboard):
    assert repr(get_keyboard) == "Keyboard('Dark Project KD87A', 9600, 5)"


def test_str(get_keyboard):
    assert str(get_keyboard) == 'Dark Project KD87A'


def test_add(get_keyboard):
    assert get_keyboard + get_keyboard == get_keyboard.quantity + get_keyboard.quantity

    with pytest.raises(TypeError):
        get_keyboard + 50

def test_lang(get_keyboard):
    assert get_keyboard.language == 'EN'

    get_keyboard.change_lang()
    assert get_keyboard.language == 'RU'

    with pytest.raises(AttributeError):
        get_keyboard.language = 'ss'