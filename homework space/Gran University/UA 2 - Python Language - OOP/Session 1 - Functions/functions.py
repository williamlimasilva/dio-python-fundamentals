#Create a simple function showing the result of two numbers, give the treatment of the exception of division by zero and the parameters will be inserted by the user.
def calculator():
    while True:
        print("\nSelect the operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        operation = input("Enter the number of the operation 1 2 3 4: ")

        if operation not in ('1', '2', '3', '4'):
            print("Invalid operation. Please select a valid option.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Error: Please enter valid numbers.")
            continue

        match operation:
            case '1':
                result = num1 + num2
                op_symbol = '+'
            case '2':
                result = num1 - num2
                op_symbol = '-'
            case '3':
                result = num1 * num2
                op_symbol = '*'
            case '4':
                try:
                    result = num1 / num2
                except ZeroDivisionError:
                    print("Error: Division by zero is not allowed.")
                    continue
                op_symbol = '/'
            case other:
                print("Error: Invalid operation! Please select a valid option.")
                continue
        print(f"The result of {num1} {op_symbol} {num2} is {result}.")

        cont = input("Would you like to perform another calculation? (y/n): ").strip().lower()
        if cont != 'y':
            print("Calculator finished.")
            break

calculator()