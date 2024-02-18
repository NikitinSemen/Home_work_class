import pytest
from Class import Category

from Class import Product


@pytest.fixture
def product_iphone():
    return Product('iphone', 'smartphone i not have takou', 12000.0, 12)


def test_init(product_iphone):
    assert product_iphone.name == 'iphone'
    assert product_iphone.price == 12000.0
    assert product_iphone.description == 'smartphone i not have takou'
    assert product_iphone.quantity == 12


@pytest.fixture()
def category():
    return Category('Смартфоны', 'телефоны с камерой и интернетом', ['iphone', 'samsung'])


def test_category_count(category):
    assert category.category_count == 0


def test_uniq_name(category):
    assert category.uniq_name == 0


def test_init_category(category):
    assert category.name == 'Смартфоны'
    assert category.description == 'телефоны с камерой и интернетом'
    assert category.products == ['iphone', 'samsung']
