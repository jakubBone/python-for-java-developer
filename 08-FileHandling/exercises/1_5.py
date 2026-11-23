# A program that prints the list of countries from a file, numbered.

counter = 1
with open('countries.txt', 'r') as file:
    for line in file:
        # strip() removes the newline character (and spaces) from both ends of the line
        print(f'{counter}. {line.strip()}')
        counter += 1
