#create a multiplication table for all numbers from 1 to 10 using a for loop
for i in range(1, 11):
    print(f"\nMultiplication table for {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")