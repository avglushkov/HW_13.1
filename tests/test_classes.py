from src.utils.classes import Category, Product, ProdItereation

import pytest


@pytest.fixture()
def categories():
    """ Задаем для тестов три экземпляра категорий"""
    category1 = Category('Ножи', 'Разные ножи', ['Столовые', 'Финки'])
    category2 = Category('Кастрюли', 'Разные кастрюли', ['2 литра', '3 литра', '12 литров'])
    category3 = Category('Сковороды', 'Разные сковороды', ['22 см', '24 см', '28 см'])

    return category1, category2, category3


def test_categories(categories):
    """Тестируем корректность атрибутов класса Category"""
    category1, category2, category3 = categories
    assert category1.category_name == 'Ножи'
    assert category1.category_discription == 'Разные ножи'
    assert category1._category_products[0] == 'Столовые'
    assert category1._category_products[1] == 'Финки'

    assert Category.categories_amount == 3 # Проверка расчета количества экземпляров класса
    assert Category.category_products_amount == 8 # Проверка корректности расчета количества уникальныех продуктов

@pytest.fixture()
def tst_products():
    """Задаем тестовые данные"""

    return [{'category_name': 'Смартфоны', 'category_description': 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни',
             'category_products': [{'product_name': 'Samsung Galaxy C23 Ultra', 'product_description': '256GB, Серый цвет, 200MP камера', 'product_price': 180000.0, 'product_amount': 5},
                          {'product_name': 'Iphone 15', 'product_description': '512GB, Gray space', 'product_price': 210000.0, 'product_amount': 8},
                          {'product_name': 'Xiaomi Redmi Note 11', 'product_description': '1024GB, Синий', 'product_price': 31000.0, 'product_amount': 14}]},
            {'category_name': 'Телевизоры', 'category_description': 'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником',
             'category_products': [{'product_name': '55" QLED 4K', 'product_description': 'Фоновая подсветка', 'product_price': 123000.0, 'product_amount': 7}]}]


def test_Product_str(tst_products):
    """Проверка корректности вывода строкового отображения категории продуктов"""

    tst_category = Category(tst_products[0]['category_name'], tst_products[0]['category_description'], tst_products[0]['category_products'])

    assert tst_category.__str__() == 'Продукты категории Смартфоны, количество продуктов 3 шт.'

@pytest.fixture()
def tst_category_products():
    return Category(" "," ",
                        [Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5),
                         Product('Samsung Galaxy C23', '256GB, Серый цвет, 200MP камера', 100000.0, 6)])

def test_get_products(tst_category_products):
    """Проверка метода вывода вывода списка продуктов в нужном формате"""

    assert tst_category_products.get_products == ['Продукт Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.','Продукт Samsung Galaxy C23, 100000.0 руб. Остаток: 6 шт.']


@pytest.fixture()
def product1():
    """Задаем данные для проверки атрибутов класса Products"""
    return Product('Нож', 'нож из стали', 2400.78, 16)

def test_Product_str(product1):
    """Проверка корректности вывода строкового отображения продука"""

    assert product1.__str__() == 'Продукт Нож, 2400.78 руб. Остаток: 16 шт.'
def test_Product_add():
    """Проверка корректности возможности сложения двух продуктов"""

    prod1 = Product('Iphone 15', '512GB, Gray space', 210_000.0, 1)
    prod2 = Product('Xiaomi Redmi Note 11', '1024GB, Синий', 31_000.0, 2)

    assert (prod1 + prod2) == 272000.0

def test_products(product1):
    """Тестируем корректность атрибутов класса Products"""

    assert product1.product_name == 'Нож'
    assert product1.product_description == 'нож из стали'
    assert product1.product_price == 2400.78
    assert product1.product_amount == 16

def test_add_new_product(product1):
    """проверка метода добавления нового продукта для класса Product"""

    product1.add_new_product({'product_name': 'Нож', 'product_description': 'нож из стали', 'product_price': 2400.78, 'product_amount': 16})
    new_product = product1.add_new_product({'product_name':'Нож','product_description': 'нож из стали', 'product_price':2500.78, 'product_amount': 17})

    assert new_product.product_name == 'Нож'
    assert new_product.product_description == 'нож из стали'
    assert new_product.product_price == 2500.78
    assert new_product.product_amount == 33

def test_price(product1):
    """проверяем корректность работы сеттера price для класса Product"""

    product1.price = 2500
    assert product1.price == 2500

    product1.price = -1
    assert product1.price == 2500

@pytest.fixture()
def prod_iteration():
    return ProdItereation(["Ножи", "Кастрюли", "Сковороды", "Ложки"])

def test_ProdItereation(prod_iteration):
    products = []

    assert prod_iteration.category == ["Ножи", "Кастрюли", "Сковороды", "Ложки"]

    for i in prod_iteration:
        products.append(i)

    assert products == ["Ножи", "Кастрюли", "Сковороды", "Ложки"]