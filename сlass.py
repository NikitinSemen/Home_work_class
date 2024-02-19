class Product:
    """Класс продукт, с атрибутами:
    name = название продукта
    description = описание продукта
    price = цена продукта
    quantity = количество продукта"""
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс Категории товаров с атрибутами :
    name = "Название категории товара
    description = описание категории товара
     products = товары входящие в категорию
     Category_count = общее количество категорий
     uniq_name = общее количество уникальных товаров"""
    category_count = 0
    unique_products_count = 0

    def __init__(self,
                 name: str,
                 description: str,
                 products: list):
        self.name = name
        self.description = description
        self.products = products
