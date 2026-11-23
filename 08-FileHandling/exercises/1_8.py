# A program that prints the text from the file pets.txt and counts the words in it.

word_count = 0
with open('pets.txt') as file:
    for line in file:
        print(line, end="")
        # split() cuts a line into a list of words, len() gives the number of words
        word_count += len(line.split())

print()
print('Number of words:', word_count)
