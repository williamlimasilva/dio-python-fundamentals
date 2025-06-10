import os
from classes.AbstractCrud import AbstractCrud

class Product(AbstractCrud):
    # Get the absolute path to the db directory
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file = os.path.join(current_dir, 'db', 'products.json')
    
    def __init__(self, code=None, name=None, price=0, quantity=0):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def create(self):
        list = self.get()
        duplicated_item = filter(lambda p: p['code'] == self.code, list)
        if any(duplicated_item):
            raise ValueError(f"Product code {self.code} already exists.")
        else:
            super().create()