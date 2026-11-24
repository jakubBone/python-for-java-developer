# A program that counts how many registered cars come from each province of Poland.
# The first letter of a registration number identifies the province.

import csv

# a dictionary: the letter of a province --> the number of cars
province_names = {}
car_counts = {}

with open('province.csv', 'r', encoding='utf-8', newline='') as file:
    reader = csv.reader(file)
    next(reader)  # skips the header line
    for letter, name in reader:
        province_names[letter] = name
        car_counts[letter] = 0

others = 0
with open('vehicle.txt') as file:
    for line in file:
        number = line.strip()
        if number == '':
            continue
        first_letter = number[0]
        if first_letter in car_counts:
            car_counts[first_letter] += 1
        else:
            others += 1  # a letter that is not used by any province

for letter, name in province_names.items():
    print(f'{name}: {car_counts[letter]}')
print('Other letters:', others)
