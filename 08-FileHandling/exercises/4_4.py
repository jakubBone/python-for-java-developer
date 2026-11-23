# A program that prints the lines of it_company.csv by five lines and waits for the Enter key after each five.

with open('it_company.csv') as file:
    lines = file.read().splitlines()

index = 0
while index < len(lines):
    # lines[index:index + 5] is a slice of five lines (or fewer at the end of the file)
    for line in lines[index:index + 5]:
        print(line)
    index += 5
    if index < len(lines):
        # input() waits until the user presses Enter
        input('Press Enter key...')
