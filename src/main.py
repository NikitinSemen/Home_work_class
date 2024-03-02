from src.category import Product
from src.category import Category
from src.utils import get_json


def main():
    file_name = 'products.json'
    product_json = get_json(file_name)
    Product(*product_json)


if __name__ == "__main__":
    main()
