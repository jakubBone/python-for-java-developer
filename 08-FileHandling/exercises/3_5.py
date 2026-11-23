# A program that checks a username and a password entered from the keyboard using regular expressions.

import re

# read username and password from keyboard
username = input('Enter username: ')
password = input('Enter password: ')

# pattern (criteria) for username and password
# ^ is the beginning and $ is the end of the text, {6,} means "at least 6 times"
username_pattern = r'^[a-z]{6,}$'
password_pattern = r'^[A-Za-z0-9_]{8,}$'

# check if username and password are ok (match() returns None when the text does not match the pattern)
username_match = re.match(username_pattern, username)
password_match = re.match(password_pattern, password)

# print results
if username_match and password_match:
    print('Username and password are correct')
else:
    if not username_match:
        print('Incorrect username: at least 6 characters, only lowercase letters')
    if not password_match:
        print('Incorrect password: at least 8 characters, only letters, digits and underscore')
