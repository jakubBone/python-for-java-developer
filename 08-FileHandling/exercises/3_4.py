# A program that calculates the total value of money spent, based on the shopping report in the file report.txt.

import re  # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of the email (utf-8, because the text contains the euro sign)
with open(email_file, 'r', encoding='utf-8') as file:
    email = file.read()

# regular expression pattern for amounts: the euro sign followed by digits
pattern = r'€(\d+)'

# findall() returns a list of texts matched by the part of the pattern in parentheses
amounts = re.findall(pattern, email)

# calculate the total purchases
total = 0
for amount in amounts:
    total += int(amount)

# print result
print('Amounts found:', amounts)
print(f'Total money spent: €{total}')
