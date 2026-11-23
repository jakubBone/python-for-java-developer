# A program that prints the first name, last name and email of the graphic designers from it_company.csv.

import csv

print('GRAPHIC DESIGNERS')
print('=================')

with open('it_company.csv', newline='') as file:
    # DictReader reads every row as a dictionary: the keys are the column names from the first line
    reader = csv.DictReader(file)
    for row in reader:
        if row['Job Title'] == 'Graphic Designer':
            print(f"{row['First Name']} {row['Last Name']},{row['Email']}")
