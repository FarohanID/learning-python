class Book:
    TYPES = ("hardcover", "paperback", "ebook")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, {self.weight}kg>"
    
    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)

# book = Book("Python 101", "paperback", 0.5)
book = Book.paperback("Python 101", 0.5)
light = Book.paperback("Python 101", 0.1)

print(book) # Output: <Book Python 101, paperback, 0.5kg>
print(book.name) # Output: Python 101
print(book.book_type) # Output: paperback
