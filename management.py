class Library:
    def __init__(self):
        self.books = ["Python", "Java", "DBMS"]

    def add_book(self, book):
        self.books.append(book)
        print(f"{book} added")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"{book} removed")
        else:
            print("Book not found")

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"{book} issued. Take it!")
        else:
            print("Book not available")

    def return_book(self, book):
        self.books.append(book)
        print(f"{book} returned. Thank you!")

    def display_books(self):
        print("Available books:", self.books)

lib = Library()
lib.display_books()
lib.issue_book("Python")
lib.display_books()