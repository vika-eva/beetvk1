class Author:
    def __init__(self, name: str, country: str, birth: str):
        self.name = name
        self.country = country
        self.birth = birth
        self.books = []

    def __str__(self):
        return f"name author: {self.name}, country: {self.country}, years: {self.birth} - {self.books}"

    def __repr__(self):
        return f"{self.name} {self.country} {self.birth} {self.books}"

class Book:
    all_books = []
    books_amount = 0

    def __init__(self, name: str, year: int, author: "Author"):
        self.name = name
        self.year = year
        self.author = author
        Book.all_books.append(self.name)
        Book.books_amount += 1

    def __str__(self):
        return f"name book: {self.name}"

    def __repr__(self):
        return f"{self.name}"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.authors = []


    def new_book(self, name: str, year: int, author: "Author") -> Book:
        book = Book(name, year, author)
        self.books.append(self.name)
        if book not in author.books:
            author.books.append(book)
        return book

    def group_by_author(self, author: "Author") -> list:
        books_by_author = []
        for book in self.books:
            if author in book.authors:
                books_by_author.append(book)
        return books_by_author

    def group_by_year(self, year: int) -> list:
        books_by_year = []
        for book in self.books:
            if book.year == year:
                books_by_year.append(book)
        return books_by_year


    def __repr__(self):
        return f"{self.name} {self.books}"

    def __str__(self):
        return f"{self.name} {self.books}"



