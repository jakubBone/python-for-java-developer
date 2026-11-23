# A program that writes the Seven Wonders of the World to a text file in alphabetical order.

seven_wonders = [
    "Great Wall of China",
    "Petra",
    "Christ the Redeemer",
    "Machu Picchu",
    "Chichen Itza",
    "Roman Colosseum",
    "Taj Mahal"
]

# Name of the file to write to
file_name = 'seven_wonders.txt'

# Sort data alphabetically
seven_wonders = sorted(seven_wonders)

# Write data to the file, each name on a separate line
with open(file_name, 'w') as file:
    for item in seven_wonders:
        file.write(item + '\n')

print(f'The list has been written to {file_name}.')
