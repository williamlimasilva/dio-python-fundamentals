from classes.AbstractCrud import AbstractCrud

class Product(AbstractCrud):
    file = 'db/products.json'
    def __init__(self, code, name, price = 0, quantity = 0):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = quantity