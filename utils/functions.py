from pathlib import Path
import json



data_folder = Path('/home/avgl/Projects/ecom_project/data')
sourse_file = data_folder / 'products.json'
def products_data():
    """чтение данных о транзакциях из json файла """

    products = []

    with open(sourse_file, 'r', encoding = "utf-8") as f:
        products_load = f.read()
        products = json.loads(products_load)
    return products

print(products_data())