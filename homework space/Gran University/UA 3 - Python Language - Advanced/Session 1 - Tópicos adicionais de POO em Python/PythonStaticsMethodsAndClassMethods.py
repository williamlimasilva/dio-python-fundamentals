#Create a example of a class with a static method and a class method
class Example:
    @staticmethod
    def static_method():
        return "This is a static method."

    @classmethod
    def class_method(cls):
        return f"This is a class method of {cls.__name__}."
# Example usage
print(Example.static_method())  # Output: This is a static method.
print(Example.class_method())   # Output: This is a class method of Example.