# A program that reads data of a purchased product from the keyboard and saves it to the file product.json.

import json

product = {}

# read product data from keyboard
product["name"] = input('Product name: ')
product["price"] = float(input('Price: '))  # a real number
answer = input('Paid (yes/no): ')
product["paid"] = answer == 'yes'  # a bool: True only for the answer yes

# save product data to json file
with open('product.json', 'w', encoding='utf-8') as file:
    json.dump(product, file, indent=4, ensure_ascii=False)

print('Data has been written to product.json')
print(product)
