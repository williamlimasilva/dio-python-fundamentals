# create a multiplication table for a number 2 using a while loop
i = 1
continuar = True
while continuar:
    number = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

    continuar = input("Do you want to continue? (y/n): ")
    continuar = True if continuar == "y" else False