# A program that reduces the prices of a clothing store by 10% and prints them before and after the discount.

price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}


def print_prices(prices):
    total = 0
    for product, price in prices.items():
        print(f'{product}: {price:.2f}')
        total += price
    print(f'Total value: {total:.2f}')


print('Before the discount:')
print_prices(price_list)

# modifies the price list: the value of an existing key is replaced with a new one
for product in price_list:
    price_list[product] = round(price_list[product] * 0.9, 2)

print('After the 10% discount:')
print_prices(price_list)
