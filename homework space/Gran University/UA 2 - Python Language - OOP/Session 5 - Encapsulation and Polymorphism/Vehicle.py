class Vehicle:
    def __init__(self, brand: str, model: str, year: int):
        # Public attribute (no underscore)
        self.brand = brand
        # Protected attribute (single underscore)
        self._model = model
        # Private attribute (double underscore)
        self.__year = year
        # Private attribute for mileage
        self.__mileage = 0

    # Getter for protected attribute model
    @property
    def model(self):
        return self._model
    
    # Setter for protected attribute model
    @model.setter
    def model(self, value: str):
        if not value.strip():
            raise ValueError("Model cannot be empty")
        self._model = value

    # Getter for private attribute year
    @property
    def year(self):
        return self.__year
    
    # Setter for private attribute year
    @year.setter
    def year(self, value: int):
        if value < 1900:
            raise ValueError("Invalid year")
        self.__year = value

    # Getter for private attribute mileage
    @property
    def mileage(self):
        return self.__mileage
    
    # Protected method
    def _update_mileage(self, distance: float):
        if distance > 0:
            self.__mileage += distance

    # Public method
    def display_info(self):
        return f"{self.brand} {self._model} ({self.__year}) - Mileage: {self.__mileage}km"


# Example of polymorphism with inheritance
class Car(Vehicle):
    def __init__(self, brand: str, model: str, year: int, doors: int):
        super().__init__(brand, model, year)
        self._doors = doors

    # Polymorphic method - overriding display_info
    def display_info(self):
        return f"Car: {super().display_info()} - {self._doors} doors"


class Motorcycle(Vehicle):
    def __init__(self, brand: str, model: str, year: int, engine_capacity: int):
        super().__init__(brand, model, year)
        self._engine_capacity = engine_capacity

    # Polymorphic method - overriding display_info
    def display_info(self):
        return f"Motorcycle: {super().display_info()} - {self._engine_capacity}cc"


# Example usage
if __name__ == "__main__":
    # Creating instances
    car = Car("Toyota", "Corolla", 2023, 4)
    motorcycle = Motorcycle("Honda", "CBR", 2023, 600)

    # Using public methods and attributes
    print(car.brand)  # Public attribute access
    print(car.model)  # Protected attribute access through property
    
    # Updating mileage using protected method
    car._update_mileage(100)
    motorcycle._update_mileage(50)

    # Demonstrating polymorphism
    vehicles = [car, motorcycle]
    for vehicle in vehicles:
        print(vehicle.display_info())
