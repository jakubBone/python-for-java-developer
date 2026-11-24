# A program that prints a list of dictionaries with countries and their populations.

countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "Germany", "population": 83200000},
    {"name": "France", "population": 67800000},
    {"name": "Italy", "population": 59000000},
    {"name": "Spain", "population": 47400000}
]

# :<10 aligns the text to the left in a field of 10 characters
print(f"{'COUNTRY':<10}POPULATION")
for country in countries:
    print(f"{country['name']:<10}{country['population']}")
