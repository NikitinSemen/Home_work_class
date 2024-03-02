import json
from src.category import Category


def get_json(file_name):
    """Функция распаковывающая файл json в класс Product"""
    with open(file_name) as file:
        files = json.load(file)
        return files
