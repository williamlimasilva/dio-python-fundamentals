import json

class AbstractCrud:
    def detail(self):
        return self.__dict__

    def insert(self):
        items = self.consult()
        items.append(self.detail())
        with open('db/categories.json', 'w') as file:
            json.dump(items, file, indent=4)
        print(f"Item {self.name} inserido com sucesso!")
    
    def list_all(self):
        items = self.consult()
        for i,p  in enumerate(items):
            print(f"Item {i} - {p['name']}")
        return items
    
    def consult(self):
        try:
            with open('db/categories.json') as file:
                return json.load(file)
        except Exception:
            return []