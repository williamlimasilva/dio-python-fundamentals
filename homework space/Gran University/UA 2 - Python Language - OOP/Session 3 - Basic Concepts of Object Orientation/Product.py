#Create a object class called Product with a constructor that takes a name and a price and methods to get the name and price of the product.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

if __name__ == "__main__":
    # Example using __dict__
    product = Product("Laptop", 999.99)
    print("Product attributes:", product.__dict__)  # Will print: {'name': 'Laptop', 'price': 999.99}