class Catalog:
    """Manages a collection of e-books in the e-bookstore."""

    def __init__(self):
        """Initialize an empty catalog."""
        self._ebooks = []  # Protected attribute for extension

    def add_ebook(self, ebook):
        """Add an e-book to the catalog."""
        self._ebooks.append(ebook)

    def remove_ebook(self, ebook):
        """Remove an e-book from the catalog."""
        self._ebooks.remove(ebook)

    def search_ebook(self, title):
        """Search for e-books by title."""
        return [ebook for ebook in self._ebooks if title.lower() in ebook.title.lower()]

    def __str__(self):
        """String representation of the catalog."""
        return "Catalog:\n" + "\n".join([str(ebook) for ebook in self._ebooks])
