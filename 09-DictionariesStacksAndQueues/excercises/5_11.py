# A program that records voting: the results are kept in the file voting.json
# in the form {"person name": number of votes}. The program can be run many times.

import json

file_name = 'voting.json'

# Read the contents of the json file (at the first run the file does not exist yet)
try:
    with open(file_name, 'r', encoding='utf-8') as file:
        votes = json.load(file)
except FileNotFoundError:
    votes = {}

# Vote for a person
person_name = input('Name of the person you are voting for: ')
if person_name in votes:
    votes[person_name] += 1
else:
    votes[person_name] = 1  # a new person starts with one vote

# Save voting data to json file
with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(votes, file, indent=4, ensure_ascii=False)

print(votes)
