class Imovel:
    def __init__(self,name,bedrooms, suites):
        self.name = name
        self.bedrooms = bedrooms
        self.suites = suites

    def __add__(self, other):
        return self.bedrooms + other.bedrooms
    def __sub__(self, other):
        return self.bedrooms - other.bedrooms
    def __mul__(self, other):
        return self.bedrooms * other.bedrooms
    def __truediv__(self, other):
        return self.bedrooms / other.bedrooms if other.bedrooms != 0 else "Divisão por zero não é permitida"
    def __gt__(self, other):
        return self.bedrooms > other.bedrooms
    def __lt__(self, other):
        return self.bedrooms < other.bedrooms
    def __eq__(self, other):
        return self.bedrooms == other.bedrooms
    def __ne__(self, other):
        return self.bedrooms != other.bedrooms
    def __ge__(self, other):
        return self.bedrooms >= other.bedrooms
    def __le__(self, other):
        return self.bedrooms <= other.bedrooms
    def __str__(self):
        return f"Imóvel: {self.name}, Quartos: {self.bedrooms}, Suítes: {self.suites}"
    
# Exemplo de uso da classe Imovel
home = Imovel("Casa", 3, 4)
print(home.__dict__)

mansion = Imovel("Mansão", 5, 6)
print(mansion.__dict__)

print(home + mansion)
print(home < mansion)
print(home > mansion)