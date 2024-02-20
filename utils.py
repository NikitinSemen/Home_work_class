import json
from category_products import Product


def get_json(file_name):
    """Функция распаковывающая файл json в класс Product"""
    with open(file_name) as file:
        files = json.load(file)
        for f in files:
            return Product(name=f, description=f, price=f, quantity=f)