# A program that saves the employees with the position "Software Engineer" to a file.

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(employees_file) as source:
    with open(position_file, 'w') as target:
        for line in source:
            # the line already ends with a newline character, so it is written as it is
            if job_title in line:
                target.write(line)

print(f'The employees have been saved to {position_file}.')
