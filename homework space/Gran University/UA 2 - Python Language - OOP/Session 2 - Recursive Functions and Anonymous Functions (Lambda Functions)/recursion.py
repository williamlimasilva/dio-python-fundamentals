#Create a example of recursion in Python
def factorial(n):
    if n == 0:
        print("Reached base case: factorial(0) = 1")
        return 1
    else:
        result = n * factorial(n - 1)
        print(f"Result of factorial({n}) = {result}")
        return result

num = int(input("Enter a number to calculate its factorial: "))
print(f"Final result: factorial({num}) = {factorial(num)}")
    