class Category:
    name = str
    description = str
    products = list
    category_count = 0
    uniq_name = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products


class Product:
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
