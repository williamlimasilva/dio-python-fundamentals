# Create an example of a lambda function in Python
# A lambda function is a small anonymous function that can take any number of arguments but can only have one expression.	
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]