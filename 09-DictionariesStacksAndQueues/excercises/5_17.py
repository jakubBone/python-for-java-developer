# A program that prints information about the cities from the file cities.json.

import json

# encoding='utf-8' is needed because the city names contain Polish characters
with open('cities.json', 'r', encoding='utf-8') as file:
    # the file contains a list of dictionaries
    data = json.load(file)

for city in data:
    for key, value in city.items():
        print(key, ':', value)
    print()
