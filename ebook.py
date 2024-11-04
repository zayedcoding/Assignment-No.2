class EBook:
    """Represents an e-book in the catalog with details and pricing."""

    def __init__(self, title, author, publication_date, genre, price, isbn):
        """Initialize the EBook with the given details."""
        self.__title = title  # Private attribute
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price
        self.__isbn = isbn

    # Getter and setter methods
    @property
    def title(self):
        """Get the title of the e-book."""
        return self.__title

    @title.setter
    def title(self, value):
        """Set the title of the e-book."""
        self.__title = value

    @property
    def price(self):
        """Get the price of the e-book."""
        return self.__price

    @price.setter
    def price(self, value):
        """Set the price of the e-book."""
        self.__price = value

    def __str__(self):
        """String representation of the e-book."""
        return f"EBook: {self.__title}, Author: {self.__author}, Price: ${self.__price:.2f}"
