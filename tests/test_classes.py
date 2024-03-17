from utils.classes import Category, Product
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
    assert category1.category_products[0] == 'Столовые'
    assert category1.category_products[1] == 'Финки'

    assert Category.categories_amount == 3 # Проверка расчета количества экземпляров класса
    assert Category.category_products_amount == 8 # Проверка корректности расчета количества уникальныех продуктов


@pytest.fixture()
def product1():
    """Задаем данные для проверки атрибутов класса Products"""
    return Product('Нож', 'нож из стали', 2400.78, 16)


def test_products(product1):
    """Тестируем корректность атрибутов класса Products"""

    assert product1.product_name == 'Нож'
    assert product1.product_description == 'нож из стали'
    assert product1.product_price == 2400.78
    assert product1.product_amount == 16
