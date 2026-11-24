# A program that prints information about a computer from the file computer.json.

import json

# Open the JSON file in read mode
with open('computer.json', 'r', encoding='utf-8') as file:
    # json.load() turns the content of the file into a dictionary
    data = json.load(file)

# Print the JSON data
for key, value in data.items():
    print(key, ':', value)
