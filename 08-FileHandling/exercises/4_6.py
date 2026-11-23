# A program that counts the lines, characters and words of a text file given by the user.

file_name = input('File name: ')

try:
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()

    lines = len(content.splitlines())
    characters = len(content)
    words = len(content.split())

    print(f'Number of lines: {lines}')
    print(f'Number of characters: {characters}')
    print(f'Number of words: {words}')
except FileNotFoundError:
    # a file with the given name does not exist
    print(f'The file {file_name} does not exist.')
