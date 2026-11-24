# A program that copies the book data from the given genres of books.csv to the corresponding files.
# The program is divided into functions.

import csv

# Genre --> Filename
genre_files = [
    ('Fantasy', 'books_fantasy.txt'),
    ('Historical', 'books_historical.txt'),
    ('Romance', 'books_romance.txt'),
    ('Classic', 'books_classic.txt')
]


def read_books(file_name):
    # returns a list of books; every book is a list: [Title, Author, Genre, Year]
    with open(file_name, 'r', encoding='utf-8', newline='') as file:
        return list(csv.reader(file))[1:]  # [1:] skips the header line


def select_by_genre(books, genre):
    selected = []
    for book in books:
        if book[2] == genre:
            selected.append(book)
    return selected


def save_books(file_name, books):
    with open(file_name, 'w', encoding='utf-8') as file:
        for book in books:
            file.write(','.join(book) + '\n')


def main():
    books = read_books('books.csv')
    for genre, file_name in genre_files:
        selected = select_by_genre(books, genre)
        save_books(file_name, selected)
        print(f'{genre}: {len(selected)} books saved to {file_name}')

# Run main() only when this file is executed directly (not when imported as a module
if __name__ == "__main__":
    main()
