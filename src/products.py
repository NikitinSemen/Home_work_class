from abc import ABC, abstractmethod
from src.mixin_class import MixinRepr


class Goods(ABC):
    pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_quantity(self):
        pass


class Product(Goods, MixinRepr):
    """Класс продукт, с атрибутами:
    name = название продукта
    description = описание продукта
    price = цена продукта
    quantity = количество продукта"""

    def __init__(self, name: str,
                 description: str,
                 price: float,
                 quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.price}.руб. Остаток: {self.quantity} шт.'

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    @classmethod
    def new_product(cls, value):
        """
        Метод для добавления нового товара в класс
        """
        return cls(**value)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для изменения цены, на случай попытки понижение цены
        реализованна проверка"""
        if value <= 0:
            print("Введена неккоректная цена")
        elif self.__price < value:
            self.__price = value
        elif self.__price > value:
            while True:
                user_input = input("Введенная цена ниже установленной, уверены что хотите понизить цену?(y/n)").lower()

                if user_input == 'y':
                    self.__price = value
                    break
                elif user_input == 'n':
                    break

    def __add__(self, other):
        if issubclass(type(other), Product):
            first_prod = self.price * self.quantity
            second_prod = other.price * other.quantity
            return first_prod + second_prod
        else:
            raise TypeError('Не совпадают классы')


class Smartphone(Product, MixinRepr):
    """
    Класс Смартфон. Класс наследуемый от класса продуктов для выдедения абстракции товара Смартфон

    """

    def __init__(self, name, description, price, quantity, performance, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color


class GreenGrass(Product, MixinRepr):
    """
    Класс Зеленая Трава. Класс наследуемый от класса продуктов для выдедения абстракции товара Зеленая Трава
    """

    def __init__(self, name, description, price, quantity, country, germination, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination = germination
        self.color = color
