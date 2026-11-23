# A program that calculates the total number of parked cars from the file car_park.txt.


def read_from_file(name):
    with open(name) as file:
        content = file.read()
    return content


# reads the entire file and splits lines into a list
file_content = read_from_file('car_park.txt')
file_lines = file_content.splitlines()

# calculates the total number of cars parked
total = 0
for line in file_lines:
    # every line is a text, so it is converted to a number
    total += int(line)

print('Total cars parked:', total)
