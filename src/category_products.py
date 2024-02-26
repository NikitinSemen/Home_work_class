class Product:
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
        """Метод для добавления нового товара в класс"""
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
        first_prod = self.price * self.quantity
        second_prod = other.price * other.quantity
        return first_prod + second_prod
class Category:
    """Класс Категории товаров с атрибутами :
    name = "Название категории товара
    description = описание категории товара
    products = товары входящие в категорию (обьекты класса Product)
    Category_count = общее количество категорий
    uniq_name = общее количество уникальных товаров"""
    total = 0
    unique_products = set()
    unique_products_count = 0

    def __init__(self,
                 name: str,
                 description: str,
                 products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products
        Category.total += 1
        for product in products:
            Category.unique_products.add(product.name)
        Category.unique_products_count = len(Category.unique_products)

    def add_product(self, obj_product):
        """Добавляет обьект класса Product в список товара класса Category"""
        self.__products.append(obj_product)
        Category.total += 1

    def get_products(self):
        return self.__products

    @property
    def products(self):
        """Геттер для вывода товара, цены, колличества - в определенной форме"""
        list_prod = []
        for p in self.__products:
            list_prod.append(Product)
            return list_prod

    def __len__(self):
        return len(self.__products)

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self.__products)}'
