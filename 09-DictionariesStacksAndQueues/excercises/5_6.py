# A program that creates the dictionary person from two dictionaries with personal data.

basic_data = {
    "name": "Barbara",
    "age": 21
}

advanced_data = {
    "status": "student",
    "married": False,
    "interest": ["reading", "swimming"]
}

person = {}
# update() adds all key-value pairs of another dictionary
person.update(basic_data)
person.update(advanced_data)

for key, value in person.items():
    print(f'{key}: {value}')
