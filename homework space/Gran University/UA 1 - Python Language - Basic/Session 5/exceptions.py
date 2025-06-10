#create a example of exception handling
try:
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
    result = num1 / num2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("Division was successful.")
finally:
    print("Execution completed.")