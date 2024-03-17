from utils.functions import get_product, get_category
import pytest

@pytest.fixture()
def products():
    """Задаем тестовые данные"""

    return [{'name': 'Смартфоны', 'description': 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни',
             'products': [{'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый цвет, 200MP камера', 'price': 180000.0, 'quantity': 5},
                          {'name': 'Iphone 15', 'description': '512GB, Gray space', 'price': 210000.0, 'quantity': 8},
                          {'name': 'Xiaomi Redmi Note 11', 'description': '1024GB, Синий', 'price': 31000.0, 'quantity': 14}]},
            {'name': 'Телевизоры', 'description': 'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником',
             'products': [{'name': '55" QLED 4K', 'description': 'Фоновая подсветка', 'price': 123000.0, 'quantity': 7}]}]

def test_get_category(products):
    """Проверяем корректность фкнции get_category"""

    category_1 = get_category(products, 0)
    category_2 = get_category(products, 4)# задаем экземпляр класса Category, для которого нет наполнения данных в исходнике. Функция должна выдавать исключение

    assert category_1.category_name == 'Смартфоны'
    assert category_1.category_discription == 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'
    assert category_1.category_products[0] == {'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый цвет, 200MP камера', 'price': 180000.0, 'quantity': 5}

    assert category_2.category_name == 'Категория отсутствует'
    assert category_2.category_discription == '-'
    assert category_2.category_products == []

def test_get_product(products):
    """Проверяем корректность фкнции get_product"""

    product_1 = get_product(products, 0, 0)
    product_2 = get_product(products, 4, 0)# задаем экземпляр класса Category, для которого нет наполнения данных в исходнике. Функция должна выдавать исключение
    product_3 = get_product(products, 1, 5)# задаем экземпляр класса Product, для которого нет наполнения данных в исходнике. Функция должна выдавать исключение


    assert product_1.product_name == 'Samsung Galaxy C23 Ultra'
    assert product_1.product_description == '256GB, Серый цвет, 200MP камера'
    assert product_1.product_price == 180000.0
    assert product_1.product_amount == 5

    #Проверяем первое исключение, когда выбрали неправильные номер категории , выходящий из диапозона
    assert product_2.product_name == 'Категория и продукт отсутствуют'
    assert product_2.product_description == '-'
    assert product_2.product_price == 0.00
    assert product_2.product_amount == 0

    # Проверяем первое исключение, когда выбрали неправильные номер продукта, выходящий из диапозона
    assert product_3.product_name == 'Продукт отсутствует'
    assert product_3.product_description == '-'
    assert product_3.product_price == 0.00
    assert product_3.product_amount == 0

