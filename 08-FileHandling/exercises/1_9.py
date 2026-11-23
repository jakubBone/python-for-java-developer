# A program that prints the employees with the position "Software Engineer", numbered.

# Employee List
file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'

counter = 1
with open(file_name) as file:
    for line in file:
        # the in operator checks whether a text is contained in another text
        if job_title in line:
            print(f'{counter}. {line.strip()}')
            counter += 1
