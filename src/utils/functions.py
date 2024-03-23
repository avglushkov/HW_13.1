from pathlib import Path
from src.utils.classes import Category, Product
import json

data_folder = Path('/data')
sourse_file = data_folder / 'products.json'
def products_data():
    """чтение данных о продуктах из json файла """

    products = []

    with open(sourse_file, 'r', encoding = "utf-8") as f:
        products_load = f.read()
        products = json.loads(products_load)
    return products

def get_category(products, category_count):
    """Функция, которая дает возможность из файла с данными о продуктах выгрузить экземпляр класса Category, выбрав его из списка"""

    if category_count > len(products): # Проверяем на случай если мы задали слишком большой номер категории и его нет в исходном файле
        return Category('Категория отсутствует', '-', [])

    else:
        category = Category(products[category_count]['name'], products[category_count]['description'], products[category_count]['products'])
        return category

def get_product(products, category_count, product_count):
    """Функция, которая дает получить экземпляр класса Product, задав порядковый номер категории и продукта в категории"""

    if category_count > len(products):
        return Product('Категория и продукт отсутствуют', '-', 0.00, 0)
    else:
        if product_count > len(products[category_count]['products']):
            return Product('Продукт отсутствует', '-', 0.00, 0)

        else:
            product = Product(products[category_count]['products'][product_count]['name'],
                              products[category_count]['products'][product_count]['description'],
                              products[category_count]['products'][product_count]['price'],
                              products[category_count]['products'][product_count]['quantity'])
            return product