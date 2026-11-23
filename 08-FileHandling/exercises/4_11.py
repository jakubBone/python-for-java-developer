# A program that calculates, prints and saves to a file the integers from 1 to 100 and their second and third powers.

with open('powers.txt', 'w') as file:
    for n in range(1, 101):
        line = f'{n},{n ** 2},{n ** 3}'
        print(line)
        file.write(line + '\n')
