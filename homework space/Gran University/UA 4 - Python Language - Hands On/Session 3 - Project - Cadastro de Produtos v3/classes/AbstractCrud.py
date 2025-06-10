import json
import os
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
        print(f"Debug: Arquivo existe: {os.path.exists(cls.file)}")
        print(f"Debug: Items encontrados: {len(items)}")
        
        for i,p  in enumerate(items):
            props = ', '.join(f"{k}: {v}" for k, v in p.items())
            print(f"Item {i + 1} - {props}")
        if not items:
            print("Nenhum item encontrado.")
        return items

    @classmethod
    def get(cls, item_code=None):
        try:
            items = cls.__record()            
            return items[item_code] if isinstance(item_code, int) else items
        except FileNotFoundError:
            print(f"Debug: Arquivo não encontrado: {cls.file}")
            return []
        except json.JSONDecodeError:
            print(f"Debug: Erro ao decodificar JSON do arquivo: {cls.file}")
            return []
        except Exception as e:
            print(f"Debug: Erro inesperado: {e}")
            return []

    @classmethod
    def __record(cls, items=None):
        if items is None:
            # Read from file
            try:
                print(f"Debug: Tentando abrir arquivo...")
                with open(cls.file, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    return data
            except FileNotFoundError:
                print(f"Debug: Arquivo não encontrado, criando lista vazia")
                return []
        else:
            # Write to file
            os.makedirs(os.path.dirname(cls.file), exist_ok=True)
            with open(cls.file, 'w', encoding='utf-8') as file:
                json.dump(items, file, indent=4, ensure_ascii=False)