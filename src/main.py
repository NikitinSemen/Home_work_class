from src.category_products import Product
from src.category_products import Category
from src.utils import get_json


def main():
    file_name = 'products.json'
    product_json = get_json(file_name)
    for i in product_json:
        print(i)


if __name__ == "__main__":
    main()
