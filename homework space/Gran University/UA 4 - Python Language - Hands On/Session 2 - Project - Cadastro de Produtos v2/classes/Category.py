from classes.AbstractCrud import AbstractCrud

class Category(AbstractCrud):
    file = 'db/categories.json'
    def __init__(self, name):
        self.name = name    