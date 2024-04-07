from abc import ABC, abstractmethod

class Abs_product(ABC):
    """ Абстрактный класс для одъектов класса Product и его наследников """
    @abstractmethod
    def __init__(self):
        pass

class MixinLog:
    """ Класс миксинов для вывода данных об экземплярах класса продукт и его наследников с их параметрами """

    def __repr__(self):

        return (f"Объект класса  {self.__class__.__name__}: {self.product_name}, {self.product_description}, цена: {self.product_price} руб., количество: {self.product_amount}")

class ZeroProductError(Exception):
    """ Окласс исключения, который отвечает за обработку событий, когда в «Категорию» или в «Заказ» добавляется товар с нулевым количеством """

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Количество товаров должно быть не меньше 1'

    def __str__(self):
        return self.message

class Product(Abs_product, MixinLog):
    """ Задаем класс Product """
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


    def __str__(self):
        """ строковое отображение в виде: Название продукта, 80 руб. Остаток: 15 шт."""

        return f'Продукт {self.product_name}, {self.product_price} руб. Остаток: {self.product_amount} шт.'

    def __add__(self, other):
        """ возможность складывать объекты между собой таким образом,
            чтобы результат выполнения сложения двух продуктов был сложением
            сумм, умноженных на количество на складе """
        prod_class = type(self)
        other_prod_class = type(other)

        if prod_class == other_prod_class:
            return (self.product_price * self.product_amount + other.product_price * other.product_amount)

        else:
            raise ValueError('Вы пытаетесь сложить товары разных классов')



    @classmethod
    def add_new_product(cls, product):
        """ метод, который создает товар и возвращает объект, который можно добавлять в список товаров. Добавлена проверка наличия
        такого же товара, схожего по имени.В случае если товар уже существует, добавляется количество в наличии старого товара и нового.
        При конфликте цен выбрается более высокая."""

        new_product = cls(product["product_name"], product["product_description"], product["product_price"], product["product_amount"])

        try:
            if new_product.product_amount > 0:

                for prod in cls.products:
                    if prod.product_name == new_product.product_name:
                        prod.product_amount += new_product.product_amount
                        prod.product_price = max(prod.product_price, new_product.product_price)
                        return prod
                cls.products.append(new_product)
                return new_product
            else:
                raise ZeroProductError()


        except ZeroProductError as e:
            print(e)

        else:
            print('Новый товар добавлен')

        finally:
            print('Операция завершена')



    @property
    def price(self):
        """ Геттер для получения цены товара """
        return self.product_price

    @price.setter
    def price(self, new_price):
        """ Сеттер для установки новой цены товара с проверками корректности и разницы текущей и новой цены и
        подтверждением выбора новой цены """

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



class Smartphone(Product, MixinLog):

    """Класс Смартфон. Дочерний класс класса Product"""

    def __init__(self, product_name, product_description, product_price, product_ammount, model, color, performance, ram_on_board):
        super().__init__(product_name, product_description, product_price, product_ammount)
        self.model = model
        self.color = color
        self.performance = performance
        self.ram_on_board = ram_on_board

class Grass(Product, MixinLog):
    """Класс Газонная трова. Дочерний класс класса Product"""
    color: str
    country: str
    germination_period: str

    def __init__(self, product_name, product_description, product_price, product_ammount, color, country, germination_period):
        super().__init__(product_name, product_description, product_price, product_ammount)
        self.color = color
        self.country = country
        self.germination_period = germination_period


class Abs_Category(ABC):
    """ Абстрактный класс для классов Category и Order """
    def __init__(self):
        pass

class Category(Abs_Category):
    """ Класс объекта Category """
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

    def add_product(self, product) -> list[Product]:
        """ метод, который принимает на вход объект товара и добавлять его в список """

        if issubclass(type(product), Product):
           if product not in self._category_products:

               if product.product_amount <= 0:
                   raise ValueError('Количество товара должно быть не меньше одного')
               else:
                   self._category_products.append(product)
                   return self._category_products
        else:
            raise ValueError('Добавляемый объект не является экземпляром класса Product или его наследником')


    def __str__(self):
        """ Строковое отображение в виде: Название категории, количество продуктов: 200 шт """

        return f'Продукты категории {self.category_name}, количество продуктов {len(self._category_products)} шт.'


    @property
    def get_products(self):
        """ метод, который выводит список товаров в формате "Продукт, 80 руб.Остаток: 15  шт." """
        products = []
        for product in self._category_products:
            if product not in products:
                products.append(str(product))
        return products


    def average_price(self):

        """Метод расчета среднего ценника в категории"""

        products_in_category = self._category_products
        positions = 0
        summ = 0

        for i in products_in_category:
            summ += i.product_price
            positions += 1

        try:
            result = summ / positions
            return result

        except ZeroDivisionError:
            print('Количество товара должно быть не меньше одного')
            return 0


# sts_cat = Category('Колеса',
#                     'Колеса для легковых авто',
#                     [Product('Pirelli', "итальянские колеса", 10_000.0, 24),
#                      Product("Кама", "Наши колеса", 1_500.0, 4)])
#
#
# print(sts_cat.average_price())



# sts_cat.add_product(Grass('Трава1', 'газонная трава, цена за квадратный метр', 7.0, 0, 'Изумруд', 'Россия', '1 месяц'))

class Order(Abs_Category):
    """Класс Заказа"""

    order_product_name: str
    order_product_amount: int
    order_product_price: float
    order_product_summ: float

    def __init__(self, order_product_name, order_product_amount, order_product_price):

        try:

            if order_product_amount > 0:

                self.order_product_name = order_product_name
                self.order_product_amount = order_product_amount
                self.order_product_price = order_product_price
                self.order_product_summ = order_product_price * order_product_amount

            else:
                raise ZeroProductError()

        except ZeroProductError as e:
            print(e)

        else:
            print('Новый товар добавлен')

        finally:
            print('Операция завершена')

    def __str__(self):

        return f'{self.order_product_name},{self.order_product_summ}'


class ProdItereation:

    category: list
    def __init__(self, category):
        self.category = category

    def __iter__(self):
        """
        Магический метод, который создает объект для итераций
        """
        self.current_value = -1
        return self

    def __next__(self):
        """
        Магический метод, который возвращает очередной элемент
        при выполнении итерации
        """

        if self.current_value + 1 < len(self.category):
            self.current_value += 1

            return self.category[self.current_value]
        else:
            raise StopIteration


