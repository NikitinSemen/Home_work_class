import pytest
from сlass import Category

from сlass import Product


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


# def test_category_count(category):
#     assert category.category_count == 0
#
#
# def test_uniq_name(category):
#     assert category.uniq_name == 0

def test_categories_count():
    assert Category.category_count == 0
    Category('name_1', 'desc_1', ['iphone', 'samsung'])
    Category.category_count += 1
    assert Category.category_count == 1

    Category('name_2', 'desc_2', ['iphone', 'samsung'])
    Category.category_count += 1
    assert Category.category_count == 2

def test_unique_products_count():
    cheap_milk = Product('milk', '', 10, 1)
    expensive_milk = Product('milk', '', 100, 1)
    bread = Product('bread', '', 20, 1)

    category = Category(
        'name', 'desc', products=[cheap_milk, expensive_milk, bread]
    )
    assert category.unique_products_count == 2
    
def test_init_category(category):
    assert category.name == 'Смартфоны'
    assert category.description == 'телефоны с камерой и интернетом'
    assert category.products == ['iphone', 'samsung']
