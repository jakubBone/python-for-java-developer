# A program that displays the last ten Euro exchange rates from the file euro.json (data of the National Bank of Poland).
# The file was downloaded from https://api.nbp.pl/api/exchangerates/rates/c/eur/last/10/?format=json

import json

with open('euro.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

print('Date            Buying Rate     Selling Rate')
print('============================================')
# data["rates"] is a list of dictionaries: effectiveDate, bid (buying rate) and ask (selling rate)
for rate in data['rates']:
    print(f"{rate['effectiveDate']}      {rate['bid']:<15.4f} {rate['ask']:.4f}")
