import os
from classes.AbstractCrud import AbstractCrud

class Category(AbstractCrud):    
    # Get the absolute path to the db directory
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file = os.path.join(current_dir, 'db', 'categories.json')

    def __init__(self, name):
        self.name = name    