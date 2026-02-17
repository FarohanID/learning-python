class TooManyPagesError(ValueError):
    pass

class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.page_read = 0

    def __repr__(self):
        return (
            f"<book {self.name} page_count={self.page_count} page_read={self.page_read}>"
        )
    
    def read(self, pages: int):
        if self.page_read + pages > self.page_count:
            raise TooManyPagesError(
                f"You cannot read {pages} pages. You only have {self.page_count - self.page_read} pages left to read."
            )
        self.page_read += pages
        print(f"You have now read {self.page_read} pages out of {self.page_count}.")

python101 = Book("Python 101", 50)

try:
    python101.read(35)
    python101.read(50)
except TooManyPagesError as e:
    print(e)