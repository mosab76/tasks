class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.__isbn = isbn      #
        self.available = True

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.__isbn}")
        print(f"Available: {self.available}")
        print("-" * 30)

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, new_isbn):
        self.__isbn = new_isbn


class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.__membership_id = membership_id  #
        self.borrowed_books = []

    def get_membership_id(self):
        return self.__membership_id

    def set_membership_id(self, new_id):
        self.__membership_id = new_id

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print("Book is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print("This book was not borrowed by the member.")


class StaffMember(Member):
    def __init__(self, name, membership_id, staff_id):
        super().__init__(name, membership_id)
        self.staff_id = staff_id

    def add_book(self, library, book):
        library.add_book(book)
        print(f"{self.name} added book: {book.title}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            book.display_info()



    
library = Library()

book1 = Book("Python", "Ali Ahmed", "12345")
book2 = Book("OOP", "Sara Mohamed", "67890")

member1 = Member("Ahmed", "M001")

staff1 = StaffMember("Omar", "S001", "ST100")

staff1.add_book(library, book1)
staff1.add_book(library, book2)

print("\nLibrary Books:")
library.display_books()

member1.borrow_book(book1)

print("\nAfter Borrowing:")
library.display_books()

member1.return_book(book1)

print("\nAfter Returning:")
library.display_books()
