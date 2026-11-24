# A program that translates a word from English to Polish using a dictionary.

translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}

word = input('Enter a word in English: ')

# the in operator checks whether the key is in the dictionary
if word in translations:
    print(f'{word} -> {translations[word]}')
else:
    print('The translation is not available.')
