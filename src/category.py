from src.products import Product
from src.mixin_class import MixinRepr


class Category(MixinRepr):
    """Класс Категории товаров с атрибутами :
    name = "Название категории товара
    description = описание категории товара
    products = товары входящие в категорию (обьекты класса Product)
    Category_count = общее количество категорий
    uniq_name = общее количество уникальных товаров"""
    total = 0
    unique_products = set()
    unique_products_count = 0

    def __init__(self, name: str, description: str, products: list[Product], *args, **kwargs):

        self.name = name
        self.description = description
        self.__products = products
        Category.total += 1
        for product in products:
            Category.unique_products.add(product.name)
        Category.unique_products_count = len(Category.unique_products)
        super().__init__(*args, **kwargs)

    def add_product(self, obj_product):
        """Добавляет обьект класса Product в список товара класса Category"""
        if isinstance(obj_product, Product):
            self.__products.append(obj_product)
        Category.total += 1

    def get_average(self):
        total_sum = 0
        total_quantity = 0
        try:
            for product in self.__products:
                total_sum += product.price * product.quantity
                total_quantity += product.quantity
                return int(total_sum / total_quantity)
        except ZeroDivisionError('В категории нет товаров'):
            return 0

    def get_products(self):
        return self.__products

    @property
    def products(self):
        """Геттер для вывода товара, цены, колличества - в определенной форме"""
        return self.__products

    def __len__(self):
        return len(self.__products)

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self.__products)}'


# phone = Product('infinix', 'green', 12000.0, 0)
# green = Product('weed', 'nice weed', 15, 0)

gugu = Category('телефоны', "хорошие")
lala = gugu.get_average()
print(lala)
