# A program that creates a shopping list: product names entered from the keyboard are saved to a file.

# shopping list file name
shopping_list = 'shopping_list.txt'


# adds product name at the end of a shopping list
def add_product(file_name, product_name):
    # 'a' (append) adds data at the end of the file instead of overwriting it
    with open(file_name, 'a') as file:
        file.write(product_name + '\n')


# Takes next product name from the keyboard
product = ""
while product != "0":
    product = input('Enter product name (0 stops): ')
    if product == '0':
        break  # stops entering product names
    else:
        add_product(shopping_list, product)
