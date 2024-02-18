import json
from Class import Product


def get_json(file_name):
    with open(file_name) as file:
        files = json.load(file)
        for f in files:
            return Product(name=f, description=f, price=f, quantity=f)