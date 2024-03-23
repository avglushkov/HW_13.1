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
        self._category_products = category_products
        Category.categories_amount += 1 # количество экземпляров в классе категорий
        Category.category_products_amount += len(self._category_products) # количество уникальных продуктов во всех категориях товаров


    def add_product(self, product):
        """метод, который принимает на вход объект товара и добавлять его в список"""

        if product not in self._category_products:
            self._category_products.append(product)
        return self._category_products


    @property
    def get_products(self):
        """метод, который выводит список товаров в формате "Продукт, 80 руб.Остаток: 15  шт." """
        products = []
        for product in self._category_products:
            if product not in products:
                products.append(f'Продукт {product['product_name']} {product['product_price']}руб. Остаток: {product['product_amount']} шт.')
        return products



class Product:
    """Задаем класс Product"""
    product_name: str
    product_description: str
    product_price: float
    product_amount: int

    products = []

    def __init__(self, product_name, product_description, product_price, product_amount):
        self.product_name = product_name
        self.product_description = product_description
        self.product_price = product_price
        self.product_amount = product_amount

    @classmethod
    def add_new_product(cls, product):
        """метод, который создает товар и возвращает объект, который можно добавлять в список товаров.
        Добавлена проверка наличия такого же товара, схожего по имени.
        В случае если товар уже существует, добавляется количество в наличии старого товара и нового.
        При конфликте цен выбрается более высокая. """

        new_product = cls(product["product_name"], product["product_description"], product["product_price"], product["product_amount"])

        for prod in cls.products:
            if prod.product_name == new_product.product_name:
                prod.product_amount += new_product.product_amount
                prod.product_price = max(prod.product_price, new_product.product_price)
                return prod
        cls.products.append(new_product)
        return new_product


    @property
    def price(self):
        """Геттер для получения цены товара"""
        return self.product_price

    @price.setter
    def price(self, new_price):
        """Сеттер для установки новой цены товара с проверками корректности и разницы текущей и новой цены и подтверждением выбора новой цены"""

        if new_price > 0:
            if new_price >= self.product_price:
                self.product_price = new_price
                print(f'Новая цена товара {new_price}')
            elif new_price < self.product_price and input("Подтверждаете снижение цены товара? y/n\n") == 'y':
                self.product_price = new_price
                print(f'Новая цена товара {new_price}')
            else:
                print('Цена не изменилась')
        else:
            print("Введеная цена некорректна")

# test_product = Product('Нож', 'просто нож', 999.0, 4)
# print(test_product.price)
# test_product.price = 900
