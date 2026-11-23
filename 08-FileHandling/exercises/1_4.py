# A program that reads a text file line by line and prints each line.

with open('countries.txt', 'r') as file:
    # for takes the file line by line
    for line in file:
        # every line ends with a newline character, so print() must not add another one: end=""
        print(line, end="")

print()
