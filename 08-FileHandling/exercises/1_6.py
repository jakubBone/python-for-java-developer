# A program that prints the list of countries from a file, sorted alphabetically.


def read_from_file(name):
    with open(name, 'r') as file:
        content = file.read()
    return content


# reads the entire file
file_content = read_from_file('countries.txt')

# splits the entire file contents into lines and stores them in a list
file_lines = file_content.splitlines()

# sorted() returns a new, alphabetically sorted list
for line in sorted(file_lines):
    print(line)
