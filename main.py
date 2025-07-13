from models.admin import Admin

def main():
    admin = Admin("Ahmed")
    admin.add_book("Python OOP", "Ahmed Ibrahim")
    admin.add_book("Django Basics", "Creativity Code")
    admin.display_books()

if __name__ == "__main__":
    main()