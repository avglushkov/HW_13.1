class Category:
    """Класс объекта Category"""
    category_name: str
    category_discription: str
    category_products: list
    categories_amount = 0
    category_products_amount = 0


    def __init__(self, category_name, category_discription, category_products):
        self.category_name = category_name
        self.category_discription = category_discription
        self.category_products = category_products
        Category.categories_amount += 1 # количество экземпляров в классе категорий
        Category.category_products_amount += len(self.category_products) # количество уникальных продуктов во всех категориях товаров

class Product:
    """Задаем класс Product"""
    product_name: str
    product_description: str
    product_price: float
    product_amount: int

    def __init__(self, product_name, product_description, product_price, product_amount):
        self.product_name = product_name
        self.product_description = product_description
        self.product_price = product_price
        self.product_amount = product_amount


