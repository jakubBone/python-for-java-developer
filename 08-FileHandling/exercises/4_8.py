# A program that prints the file names from files.txt whose extension has exactly four characters (e.g. .html).

import re

with open('files.txt') as file:
    for line in file:
        name = line.strip()
        # a dot (.) in regex means 'any' character, so is written as \.
        # written as \., exactly four word characters, and then the end of the text 
        if re.search(r'\.\w{4}$', name):
            print(name)
