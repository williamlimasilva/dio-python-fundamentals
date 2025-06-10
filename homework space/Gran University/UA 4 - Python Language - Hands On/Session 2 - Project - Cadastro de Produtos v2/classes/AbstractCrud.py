import json
from abc import ABC  # Abstract Base Class for CRUD operations

class AbstractCrud(ABC):
    def detail(self):
        return self.__dict__

    def create(self):
        items = self.get()
        items.append(self.detail())
        self.__record(items)
        print(f"Item {self.name} inserido com sucesso!")
    
    def update(self, item_code):
        items = self.get()
        items[item_code] = self.detail()        
        self.__record(items)
        print(f"Item {self.name} atualizado com sucesso!")

    @classmethod
    def delete(cls, item_code):
        items = cls.get()
        del items[item_code]
        cls.__record(items)
        print(f"Item removido com sucesso!")

    @classmethod
    def list(cls):
        items = cls.get()
        for i,p  in enumerate(items):
            props = ', '.join(f"{k}: {v}" for k, v in p.items())
            print(f"Item {i} - {props}")
        if not items:
            print("Nenhum item encontrado.")
        return items

    @classmethod
    def get(cls, item_code=None):
        try:
            items = cls.__record()                
            return items[item_code] if isinstance(item_code, int) else items
        except Exception:
            return []

    @classmethod
    def __record(cls, items=None):
        if items is None:
            # Read from file
            try:
                with open(cls.file, 'r') as file:
                    return json.load(file)
            except FileNotFoundError:
                return []
        else:
            # Write to file
            with open(cls.file, 'w') as file:
                json.dump(items, file, indent=4)