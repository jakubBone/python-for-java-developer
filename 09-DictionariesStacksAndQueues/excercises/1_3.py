# A program that describes a mobile phone with a dictionary and prints it.

mobile = {
    "OS": "Android",
    "brand": "Samsung",
    "model": "Galaxy S23",
    "memory_GB": 256,
    "screen_inches": 6.1,
    "color": "black"
}

# items() gives the pairs (key, value), so both can be taken in the for loop
for key, value in mobile.items():
    print(f"{key} : {value}")
