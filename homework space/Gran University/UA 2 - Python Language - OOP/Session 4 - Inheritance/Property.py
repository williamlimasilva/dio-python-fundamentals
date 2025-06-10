from abc import ABC, abstractmethod

class Property(ABC):
    def __init__(self="", name="", uf="", price="", address="", area=""):
        self.name = name
        self.uf = uf
        self.price = price
        self.address = address
        self.area = area
    
    @abstractmethod
    def details(self):
        pass

    def calculateFees(self):
        return self.price * 0.02