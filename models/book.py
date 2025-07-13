class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_info(self):
        return f"{self.__title} by {self.__author}"