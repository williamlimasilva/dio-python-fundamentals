#Create a example of lambda function in Python
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers)) 
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
# Create an example of a filter function in Python
# A filter function is used to filter elements from a list based on a condition.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]