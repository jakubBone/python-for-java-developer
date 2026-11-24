# A program that writes a dictionary describing a favourite movie to the file favourite.json.

import json

favourite = {
    "title": "Inception",
    "director": "Christopher Nolan",
    "year": 2010,
    "genres": ["science fiction", "thriller"],
    "rating": 8.8,
    "seen_in_cinema": True
}

with open('favourite.json', 'w', encoding='utf-8') as file:
    json.dump(favourite, file, indent=4, ensure_ascii=False)

print('Data has been written to favourite.json')
