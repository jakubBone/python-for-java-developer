# A program that prints a summary of the hotel reservations from the file reservations.json.

import json


def load_reservations(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['reservations']


def count_rooms(reservations):
    # a set keeps every room number only once
    rooms = set()
    for reservation in reservations:
        rooms.add(reservation['room_number'])
    return len(rooms)


def count_by_payment(reservations, paid):
    count = 0
    for reservation in reservations:
        if reservation['paid'] == paid:
            count += 1
    return count


def value_by_payment(reservations, paid):
    total = 0
    for reservation in reservations:
        if reservation['paid'] == paid:
            # the value of a reservation: the number of nights times the price per night
            total += reservation['nights'] * reservation['price_per_night']
    return total


reservations = load_reservations('reservations.json')

print('Number of rooms:', count_rooms(reservations))
print('Number of paid reservations:', count_by_payment(reservations, True))
print('Number of unpaid reservations:', count_by_payment(reservations, False))
print(f'Total value of paid reservations: {value_by_payment(reservations, True):.2f}')
print(f'Total value of unpaid reservations: {value_by_payment(reservations, False):.2f}')
