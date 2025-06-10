#create a array bidimensional
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# print the array
for row in matrix:
    for col in row:
        print(col, end=' ')
    print()