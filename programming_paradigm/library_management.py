class Book:
    def init(self, title: str, author: str):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out"""
        if self._is_checked_out:
            raise ValueError("Book is already checked out")
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned/available"""
        if not self._is_checked_out:
            raise ValueError("Book wasn't checked out")
        self._is_checked_out = False

    def is_available(self):
        """Check if the book is available"""
        return not self._is_checked_out

    def str(self):
        return f"{self.title} by {self.author}"


class Library:
    def init(self):
        self._books = []  # Private list to store books

    def add_book(self, book: Book):
        """Add a new book to the library"""
        self._books.append(book)

    def check_out_book(self, title: str):
        """Check out a book by title"""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        raise ValueError(f"Book '{title}' not found or already checked out")

    def return_book(self, title: str):
        """Return a book by title"""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        raise ValueError(f"Book '{title}' not found or already returned")

    def list_available_books(self):
        """List all available books"""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books currently available")
        else:
            for book in available_books:
                print(book)