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
        self.__category_products = category_products
        Category.categories_amount += 1 # количество экземпляров в классе категорий
        Category.category_products_amount += len(self.__category_products) # количество уникальных продуктов во всех категориях товаров


    def add_product(self, product):
        if product not in self.__category_products:
            self.__category_products.append(product)
        return self.__category_products


    @property
    def get_products(self):
        products = []
        for product in self.__category_products:
            if product not in products:
                products.append(f'Продукт {product.product_name} руб. Остаток: {product.product_amount} шт.'))
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


    @classmetod
    def product_add(cls, product):
        new_product = cls(product["product_name"], product["product_description"], product["product_price"], product["product_amount"])

            for prod in cls.__products:
                if prod.product_name == new_product.product_name:
                    prod.product_amount += new_product.product_amount
                    prod.product_price = max(prod.product_price, new_product.product_price)
                    return prod
            cls.products.append(new_product)
            return new_product

    @property
    def price(self):
        return self.product_price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            if new_price >= self.product_price:
                self.product_price = new_price
                print(f'Новая цена товара {new_price}')
            elif new_price < self.product_price and input("Подтверждаете снижение цены товара? y/n") == 'y':
                self.product_price = new_price
                print(f'Новая цена товара {new_price}')
            else:
                print('Цена не изменилась')
        else:
            print("Введеная цена некорректна")