# A program that compares the average room price in hotels in Krakow and in Sopot.

hotels_in_Krakow = [
    {"name": "Sky", "price": 320.00},
    {"name": "Metropol", "price": 480.00},
    {"name": "New Port", "price": 420.00},
    {"name": "Aparthotel", "price": 390.00}
]

hotels_in_Sopot = [
    {"name": "Focus", "price": 510.00},
    {"name": "Aqua", "price": 345.00},
    {"name": "La Boutique", "price": 390.00},
    {"name": "Marina", "price": 410.00}
]


def hotel_list(hotels):
    # returns the hotel names separated by a comma
    names = []
    for hotel in hotels:
        names.append(hotel["name"])
    return ",".join(names)


def avg_price(hotels):
    total = 0
    for hotel in hotels:
        total += hotel["price"]
    # round() with one argument returns an integer (half values are rounded to the nearest even number)
    return round(total / len(hotels))


krakow_price = avg_price(hotels_in_Krakow)
sopot_price = avg_price(hotels_in_Sopot)

print('Hotels in Krakow:', hotel_list(hotels_in_Krakow))
print('Average hotel price in Krakow:', krakow_price)
print('Hotels in Sopot:', hotel_list(hotels_in_Sopot))
print('Average hotel price in Sopot:', sopot_price)

if krakow_price < sopot_price:
    print('Cheaper hotels in: Krakow')
elif sopot_price < krakow_price:
    print('Cheaper hotels in: Sopot')
else:
    print('The prices are the same')
