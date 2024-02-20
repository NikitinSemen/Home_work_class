class Product:
    """Класс продукт, с атрибутами:
    name = название продукта
    description = описание продукта
    price = цена продукта
    quantity = количество продукта"""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
    def metod(self):
        return self.name

class Category:
    """Класс Категории товаров с атрибутами :
    name = "Название категории товара
    description = описание категории товара
     products = товары входящие в категорию
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
        self.products = products
        Category.total += 1
        for product in products:
            Category.unique_products.add(product.name)
        Category.unique_products_count = len(Category.unique_products)

