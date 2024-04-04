from src.utils.classes import Category, Product, ProdItereation, Grass, Smartphone, Order

import pytest

######## Тестирование класса Category его методов и наследников
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

### тестирование класса Order его атрибутов, методов и наследников
def test_order():
    """проверка корректности атрибутов класса Order"""
    prod1 = Order('Нож', 10.0, 34)
    assert prod1.order_product_summ == 340.0

### тестирование класса Product его атрибутов, методов и наследников
@pytest.fixture()
def tst_products():
    """Задаем тестовые данные - список продуктов"""

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
    grass1 = Grass('Трава1', 'газонная трава, цена за квадратный метр', 7.0, 1000, 'Изумруд', 'Россия', '1 месяц')
    grass2 = Grass('Трава2', 'газонная трава, цена за квадратный метр', 9.0, 1300, 'Изумруд', 'Россия', '1 месяц')
    phone1 = Smartphone('IPhone', 'new Iphone 15 Pro', 100_000.0, 1, 'Iphone 15 Pro', 'titan white', 200, '256')
    phone2 = Smartphone('Galaxy 23 Ultra', 'new Samsung Phone', 105_000.0, 1, 'Galaxy 23 Ultra', 'black', 300, '512')

    assert (prod1 + prod2) == 272000.0
    assert (grass1 + grass2) == 18700.0
    assert (phone1 + phone2) == 205_000.0

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

@pytest.fixture()
def tst_product_category():
    return Category('Колеса',
                    'Колеса для легковых авто',
                    [Product('Pirelli', "итальянские колеса", 10_000.0, 24),
                     Product("Кама", "Наши колеса", 1_500.0, 4)])

def test_add_product_exeption(tst_product_category):
    """проверка ошибки добавления некорректного экземпляра"""

    tst_cat = tst_product_category

    with pytest.raises(ValueError):
        tst_cat.add_product("какой то продукт")

    """проверка корректности добавления в категорию продукта наследованного класса"""

    assert str(tst_product_category.add_product(Grass('Трава1', 'газонная трава, цена за квадратный метр', 7.0, 1000, 'Изумруд', 'Россия', '1 месяц'))[2]) == 'Продукт Трава1, 7.0 руб. Остаток: 1000 шт.'

def test_price(product1):
    """проверяем корректность работы сеттера price для класса Product"""

    product1.price = 2500
    assert product1.price == 2500

    product1.price = -1
    assert product1.price == 2500

@pytest.fixture()

def tst_grass():
    return Grass('Трава1', 'газонная трава, цена за квадратный метр', 7.0, 1000, 'Изумруд', 'Россия', '1 месяц')

def test_grass(tst_grass):
    """Проверка атрибутов класса Grass"""

    assert tst_grass.country == 'Россия'
    assert tst_grass.germination_period == '1 месяц'
    assert tst_grass.color == 'Изумруд'

@pytest.fixture()
def tst_phone():
    return Smartphone('IPhone', 'new Iphone 15 Pro', 100_000.0, 1, 'Iphone 15 Pro', 'titan white', 200, '256')
def test_phone(tst_phone):
    """Проверка атрибутов класса Phone"""

    assert tst_phone.model == 'Iphone 15 Pro'
    assert tst_phone.performance == 200
    assert tst_phone.color == 'titan white'
    assert tst_phone.ram_on_board == '256'


@pytest.fixture()
def tst_mixin_products():
    return [Product('Iphone 15', '512GB, Gray space', 210_000.0, 1),
            Product('Xiaomi Redmi Note 11', '1024GB, Синий', 31_000.0, 2),
            Grass('Трава1', 'газонная трава, цена за квадратный метр', 7.0, 1000, 'Изумруд', 'Россия', '1 месяц'),
            Grass('Трава2', 'газонная трава, цена за квадратный метр', 9.0, 1300, 'Изумруд', 'Россия', '1 месяц'),
            Smartphone('IPhone', 'new Iphone 15 Pro', 100_000.0, 1, 'Iphone 15 Pro', 'titan white', 200, '256'),
            Smartphone('Galaxy 23 Ultra', 'new Samsung Phone', 105_000.0, 1, 'Galaxy 23 Ultra', 'black', 300, '512')]

def test_product_repr(tst_mixin_products):
    """проверка корректности отработки метода __repr__ в классе MixinLog для класса Product и его наследников"""

    assert repr(tst_mixin_products[1]) == 'Объект класса  Product: Xiaomi Redmi Note 11, 1024GB, Синий, цена: 31000.0 руб., количество: 2'
    assert repr(tst_mixin_products[3]) == 'Объект класса  Grass: Трава2, газонная трава, цена за квадратный метр, цена: 9.0 руб., количество: 1300'
    assert repr(tst_mixin_products[5]) == 'Объект класса  Smartphone: Galaxy 23 Ultra, new Samsung Phone, цена: 105000.0 руб., количество: 1'

### тестирование класса ProdItereation его атрибутов, методов и наследников
@pytest.fixture()
def prod_iteration():
    return ProdItereation(["Ножи", "Кастрюли", "Сковороды", "Ложки"])

def test_ProdItereation(prod_iteration):
    products = []

    assert prod_iteration.category == ["Ножи", "Кастрюли", "Сковороды", "Ложки"]

    for i in prod_iteration:
        products.append(i)

    assert products == ["Ножи", "Кастрюли", "Сковороды", "Ложки"]
