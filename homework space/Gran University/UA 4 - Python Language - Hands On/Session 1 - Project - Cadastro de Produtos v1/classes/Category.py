from classes.AbstractCrud import AbstractCrud

class Category(AbstractCrud):
    def __init__(self, name):
        self.name = name

    