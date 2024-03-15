class Category:
    category_name: str
    category_discription: str
    category_products: list
    number_of_categories = 0


    def __init__(self, category_name, category_discription, category_products):
        self.category_name = category_name
        self.category_discription = category_discription
        self.category_products = category_products
        self.number_of_categories += 1


category1 = Category('Ножи', 'Разные ножи', ['Столовые', 'Финки'])
category2 = Category('Кастрюли', 'Разные кастрюли', ['2 литра', '3 литра'])
class Product:
    product_name: str
    product_description: str
    product_price: float
    product_amount: int

    def __init__(self, product_name, product_description, product_price, product_amount):
        self.product_name = product_name
        self.product_description = product_description
        self.product_price = product_price
        self.product_amount = product_amount


print(category1.number_of_categories)
print(category2.number_of_categories)