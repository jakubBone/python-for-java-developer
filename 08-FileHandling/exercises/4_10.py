# A program that prints the products from clothing.csv whose price is less than 60 and whose stock is less than 40.

import csv

with open('clothing.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # the values read from a file are texts, so they are converted to numbers
        price = float(row['Price'])
        stock = int(row['Stock_Quantity'])
        if price < 60 and stock < 40:
            print(row['Product_Name'], row['Size'], row['Color'], price, stock)
