class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, {self.weight}g>"
    
    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[0], page_weight)
    
    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)
    
print(Book.hardcover("The Great Gatsby", 500))  # Output: <Book The Great Gatsby, hardcover, 500g>
print(Book.paperback("To Kill a Mockingbird", 300))  # Output: <Book To Kill a Mockingbird, paperback, 300g>