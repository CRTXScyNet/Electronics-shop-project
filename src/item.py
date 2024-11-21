import csv
import os
from pathlib import Path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return other.quantity + self.quantity
        raise TypeError

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.quantity * self.price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.__class__.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls, filepath):
        root_path = Path(__file__).parent.parent
        path = os.path.join(root_path, filepath)
        with open(path, newline='', encoding='ISO-8859-1') as csvfile:
            reader = csv.DictReader(csvfile)

            for line in reader:
                if len(line) != 0:
                   Item(line['name'], Item.string_to_number(line['price']), Item.string_to_number(line['quantity']))


    @staticmethod
    def string_to_number(s: str):
        return int(float(s))
