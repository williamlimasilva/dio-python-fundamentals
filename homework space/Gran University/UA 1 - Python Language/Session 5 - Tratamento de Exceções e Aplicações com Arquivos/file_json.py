#create a example of json handling
import json
# Sample data
data = [
    {
    "name": "Alice",
    "age": 30,
    "city": "New York"
    },
    {    "name": "Bob",
    "age": 25,
    "city": "Los Angeles"
    },
    {
    "name": "Charlie",
    "age": 35,
    "city": "Chicago"
    }
]

with open("data.json", "w") as file_json:
    # Write JSON data to file
    json.dump(data, file_json, indent=4)