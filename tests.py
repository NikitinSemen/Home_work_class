import pytest
from category_products import Category
from category_products import Product


@pytest.fixture
def product_iphone():
    return Product('iphone', 'smartphone i not have takou', 12000.0, 12)


def test_init(product_iphone):
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
def category():
    return Category('Смартфоны', 'телефоны с камерой и интернетом', products=[smartphone.get_name(), home_phone.get_name()])


smartphone = Product('iphone', '', 1212, 12)
home_phone = Product('Iphone', '', 1212, 12)


def test_categories_count():
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


def test_init_category(category):
    assert category.name == 'Смартфоны'
    assert category.description == 'телефоны с камерой и интернетом'
    # assert category.products == ['iphone', 'iphone']

# def test_list_products(category):
# assert category.get_products() ==
