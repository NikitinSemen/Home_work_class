import json
from src.category_products import Category


def get_json(file_name):
    """Функция распаковывающая файл json в класс Product"""
    with open(file_name) as file:
        files = json.load(file)
        for f in files:
            return Category(name=f, description=f, products=f)
