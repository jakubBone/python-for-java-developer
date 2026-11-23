# A program that counts the vowels in a text entered from the keyboard using regular expressions.

import re

text = input('Enter text: ')

# [aeiouAEIOU] matches one vowel; findall() returns the list of all matches
vowels = re.findall(r'[aeiouAEIOU]', text)

print('Number of vowels:', len(vowels))
