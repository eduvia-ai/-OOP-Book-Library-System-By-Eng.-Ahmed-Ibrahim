from models.book import Book

class Admin:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def display_books(self):
        print(f"Books managed by {self.name}:")
        for book in self.books:
            print("-", book.get_info())