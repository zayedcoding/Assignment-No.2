class ShoppingCart:
    """Represents a shopping cart containing e-books."""

    def __init__(self):
        """Initialize an empty shopping cart."""
        self._items = []  # Protected attribute

    def add_to_cart(self, ebook):
        """Add an e-book to the cart."""
        self._items.append(ebook)

    def remove_from_cart(self, ebook):
        """Remove an e-book from the cart."""
        if ebook in self._items:
            self._items.remove(ebook)

    def calculate_total(self):
        """Calculate the total cost of items in the cart."""
        return sum(item.price for item in self._items)

    def __str__(self):
        """String representation of the shopping cart."""
        return "ShoppingCart contains:\n" + "\n".join([str(item) for item in self._items])
