# This file is included for completeness but not used in this implementation
# In a production application, we would use a database with models
# instead of in-memory dictionary storage

class Book:
    """Book model representing a book in the inventory"""
    def __init__(self, isbn, title, author, price, genres):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price
        self.genres = genres
        
    def to_dict(self):
        return {
            'isbn': self.isbn,
            'title': self.title,
            'author': self.author,
            'price': self.price,
            'genres': list(self.genres)
        }
    
    @classmethod
    def from_tuple(cls, isbn, book_tuple):
        """Create a Book instance from a tuple representation"""
        title, author, price, genres = book_tuple
        return cls(isbn, title, author, price, genres)
