# A program that reads and modifies a dictionary describing a person.

# The types of the values: str, str, int, list, bool and dict (a dictionary inside a dictionary)
person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming", "excursions"],
    "married": True,
    "phone": {"landline": "123444321", "mobile": "777888999"}
}

print("Name:", person["name"])
print("Hobby:", person["hobby"])
print("The whole dictionary:", person)

# Changes surname to 'Nowak'
person["surname"] = "Nowak"

# Changes person's marriage status (not turns True into False and the other way round)
person["married"] = not person["married"]

# Adds gender: 'male' (a new key)
person["gender"] = "male"

# Adds a new hobby: 'bicycle' (the value of "hobby" is a list, so append() is used)
person["hobby"].append("bicycle")

# Adds work phone to existing phones (the value of "phone" is a dictionary)
person["phone"]["work"] = "313131444"

# Displays the entire contents of the dictionary
for key, value in person.items():
    print(f"{key}: {value}")
