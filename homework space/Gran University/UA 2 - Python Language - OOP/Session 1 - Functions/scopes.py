x = 10  # Global variable

def my_function():
    global x
    x = 20  # Modifies the global variable
    y = 5   # Local variable
    print("Inside function, x:", x)
    print("Inside function, y:", y)

my_function()
print("Outside function, x:", x)
# print("Outside function, y:", y)  # This would cause an error because y is local

