# A program that tests regular expression patterns on a text (like in the Regex101 editor).

import re

text = ("Alice was born on March 12, 1992. Her brother, John, was born on June 5, 1988. "
        "They have a mutual friend named Mike, whose phone number is 555-123-4567. "
        "In their hometown, which has a population of 1,234 or 1,235 people, "
        "a holiday festival is held every year on December 25. "
        "Alice works in an office with 30 employees. Her phone number is 555-765-4321.")

# a date "month day, year": a capital letter, small letters, a space, 1-2 digits, a comma, a space, 4 digits
date_pattern = r'[A-Z][a-z]+ \d{1,2}, \d{4}'

# a phone number XXX-XXX-XXXX: \d{3} means exactly three digits
phone_pattern = r'\d{3}-\d{3}-\d{4}'

# a number with commas as thousand separators: 1-3 digits followed by groups of a comma and 3 digits
thousands_pattern = r'\d{1,3}(?:,\d{3})+'

# a word starting with a capital letter (it also matches months and the first word of a sentence)
capital_pattern = r'\b[A-Z][a-z]+\b'

# a whole number: digits that are not a part of a date, a phone number or a number with commas
number_pattern = r'(?<![\d,-])\d+(?![\d,-])'

print('Dates:', re.findall(date_pattern, text))
print('Phone numbers:', re.findall(phone_pattern, text))
print('Numbers with commas:', re.findall(thousands_pattern, text))
print('Words starting with a capital letter:', re.findall(capital_pattern, text))
print('Whole numbers:', re.findall(number_pattern, text))
