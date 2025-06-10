import csv

# Example data to write to CSV
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'London'],
    ['Charlie', 35, 'Paris']
]

# Write data to CSV file
with open('example.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerows(data)

# Read data from CSV file
with open('example.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        print(row)
