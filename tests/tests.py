import pytest
from src.category import Category
from src.products import Product


@pytest.fixture
def product_iphone():
    return Product('iphone', 'smartphone i not have takou', 12000.0, 12)


def test_init(product_iphone):
    """Проверка инициализации класса Product"""
    assert product_iphone.name == 'iphone'
    assert product_iphone.price == 12000.0
    assert product_iphone.description == 'smartphone i not have takou'
    assert product_iphone.quantity == 12


def test_get_name(product_iphone):
    assert product_iphone.get_name() == 'iphone'


def test_get_description(product_iphone):
    assert product_iphone.get_description() == 'smartphone i not have takou'


def test_get_price(product_iphone):
    assert product_iphone.get_price() == 12000.0


def test_quantity(product_iphone):
    assert product_iphone.get_quantity() == 12


@pytest.fixture()
def category_1():
    """Инициализация класса Category"""
    return Category('Смартфоны', 'телефоны с камерой и интернетом', products=[smartphone, home_phone])


smartphone = Product('iphone', '', 1212.0, 12)
home_phone = Product('Iphone', '', 23232.0, 12)


def test_categories_count():
    """Проверка счетчика категорий"""
    assert Category.total == 0

    Category('name_1', 'desc_1', products=[smartphone, home_phone])
    assert Category.total == 1

    Category('name_2', 'desc_2', products=[smartphone, home_phone])
    assert Category.total == 2


def test_unique_products_count():
    iphone = Product('iphone', 'metal-black', 10, 1)
    expensive_iphone = Product('iphone', 'green-sea', 100, 1)
    samsung = Product('samsung', '', 20, 1)

    category = Category(
        'Смартфоны', 'телефоны с камерой и интернетом', products=[iphone, expensive_iphone, samsung]
    )
    assert category.unique_products_count == 2


@pytest.fixture()
def category_1():
    """Инициализация класса Category"""
    return Category('Смартфоны', 'телефоны с камерой и интернетом', products=[smartphone])


def test_init_category(category_1):
    assert category_1.name == 'Смартфоны'
    assert category_1.description == 'телефоны с камерой и интернетом'
    assert category_1.products == 'iphone, 1212руб. Остаток1212'


def test_category_products_getter(category_1):
    assert category_1.products == 'iphone, 1212.0руб. Остаток 12'


def test_len_product(category_1):
    assert len(category_1.products) == 1


def test_add_sum():
    phone = Product('infinix', 'green', 12000.0, 12)
    phone_1 = Product('iphone', 'white', 12000.0, 12)
    assert phone == 288000.0
