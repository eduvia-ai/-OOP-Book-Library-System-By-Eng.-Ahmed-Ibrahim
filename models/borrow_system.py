class BorrowSystem:
    def __init__(self):
        self.borrowed_books = {}

    def borrow(self, user, book):
        self.borrowed_books[user] = book

    def return_book(self, user):
        if user in self.borrowed_books:
            del self.borrowed_books[user]