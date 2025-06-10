from Property import Property

class ResidentialProperty(Property):
    def __init__(self, name="", uf="", price="", address="", area="", rooms=0, bathrooms=0):
        super().__init__(name=name, uf=uf, price=price, address=address, area=area)
        self.rooms = rooms
        self.bathrooms = bathrooms
         
    def details(self):
        base_details = super().details()
        return f"{base_details}, Rooms: {self.rooms}, Bathrooms: {self.bathrooms}"
