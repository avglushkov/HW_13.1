from utils.classes import Category, Product

import pytest

@pytest.fixture()
def category1():
    return Category('Ножи', 'Разные ножи', ['Столовые', 'Финки'])

def category2():
    return Category('Кастрюли', 'Разные кастрюли', ['2 литра', '3 литра'])

def category2():
    return Category('Сковороды', 'Разные сковороды', ['22 см', '24 см', '28 см'])

def test_init(category1)
    assert category1.category_name = 'Ножи'
    assert category1.category_description = 'Разные ножи'
    assert category1.category_products[0] = 'Столовые'
    assert category1.category_products[1] = 'Финки'

