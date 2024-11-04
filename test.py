import unittest

class EBook:
    """Represents an e-book in the catalog with details and pricing."""

    def __init__(self, title, author, publication_date, genre, price, isbn):
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price
        self.__isbn = isbn

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    def __str__(self):
        return f"EBook: {self.__title}, Author: {self.__author}, Price: ${self.__price:.2f}"

class Customer:
    """Represents a customer in the e-bookstore."""

    def __init__(self, customer_id, name, email, loyalty_member=False):
        self.__customer_id = customer_id
        self.__name = name
        self.__email = email
        self.__loyalty_member = loyalty_member

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def loyalty_member(self):
        return self.__loyalty_member

    @loyalty_member.setter
    def loyalty_member(self, value):
        self.__loyalty_member = value

    def __str__(self):
        return f"Customer: {self.__name}, Loyalty Member: {self.__loyalty_member}"

class Catalog:
    """Manages a collection of e-books in the e-bookstore."""

    def __init__(self):
        self._ebooks = []

    def add_ebook(self, ebook):
        self._ebooks.append(ebook)

    def remove_ebook(self, ebook):
        self._ebooks.remove(ebook)

    def __str__(self):
        return "Catalog:\n" + "\n".join([str(ebook) for ebook in self._ebooks])

class ShoppingCart:
    """Represents a shopping cart containing e-books."""

    def __init__(self):
        self._items = []

    def add_to_cart(self, ebook):
        self._items.append(ebook)

    def remove_from_cart(self, ebook):
        if ebook in self._items:
            self._items.remove(ebook)

    def calculate_total(self):
        return sum(item.price for item in self._items)

    def __str__(self):
        return "ShoppingCart contains:\n" + "\n".join([str(item) for item in self._items])

class Order:
    """Represents an order made by a customer."""

    def __init__(self, order_id, customer):
        self.__order_id = order_id
        self.__customer = customer
        self.cart = ShoppingCart()

    def __str__(self):
        return f"Order ID: {self.__order_id}, Customer: {self.__customer.name}\n" + str(self.cart)

class Invoice:
    """Represents an invoice for an order."""

    def __init__(self, invoice_id, order, amount_due):
        self.__invoice_id = invoice_id
        self.__order = order
        self.__amount_due = amount_due

    def __str__(self):
        return f"Invoice ID: {self.__invoice_id}, Amount Due: ${self.__amount_due:.2f}"

class DiscountPolicy:
    """Applies various discounts to orders."""

    def __init__(self):
        self.__discount_type = None
        self.__discount_value = 0.0

    def apply_loyalty_discount(self, amount):
        self.__discount_type = "loyalty"
        self.__discount_value = 0.10
        return amount * (1 - self.__discount_value)

    def apply_bulk_discount(self, amount):
        self.__discount_type = "bulk"
        self.__discount_value = 0.20
        return amount * (1 - self.__discount_value)

    def __str__(self):
        return f"Discount Type: {self.__discount_type}, Discount Value: {self.__discount_value * 100:.0f}%"

class TestEBookstore(unittest.TestCase):

    def setUp(self):
        """Set up the common test data for all test cases."""
        self.ebook1 = EBook("101 Py", "Zayed Zayed", "2021-01-01", "Programming", 29.99, "ISBN12345")
        self.ebook2 = EBook("102 Py", "Ali Zayed", "2022-02-01", "Programming", 39.99, "ISBN67890")
        self.catalog = Catalog()
        self.customer = Customer(1, "Zayed", "zayed@example.com", True)
        self.cart = ShoppingCart()
        self.discount_policy = DiscountPolicy()

    def test_add_ebook_to_catalog(self):
        """Test adding e-books to the catalog."""
        self.catalog.add_ebook(self.ebook1)
        self.catalog.add_ebook(self.ebook2)
        self.assertIn(self.ebook1, self.catalog._ebooks)
        self.assertIn(self.ebook2, self.catalog._ebooks)

    def test_remove_ebook_from_catalog(self):
        """Test removing an e-book from the catalog."""
        self.catalog.add_ebook(self.ebook1)
        self.catalog.remove_ebook(self.ebook1)
        self.assertNotIn(self.ebook1, self.catalog._ebooks)

    def test_add_to_cart(self):
        """Test adding e-books to the shopping cart."""
        self.cart.add_to_cart(self.ebook1)
        self.cart.add_to_cart(self.ebook2)
        self.assertIn(self.ebook1, self.cart._items)
        self.assertIn(self.ebook2, self.cart._items)

    def test_calculate_cart_total(self):
        """Test calculating the total cost of items in the cart."""
        self.cart.add_to_cart(self.ebook1)
        self.cart.add_to_cart(self.ebook2)
        total = self.cart.calculate_total()
        self.assertAlmostEqual(total, 29.99 + 39.99)

    def test_apply_loyalty_discount(self):
        """Test applying a loyalty discount."""
        self.cart.add_to_cart(self.ebook1)
        self.cart.add_to_cart(self.ebook2)
        total = self.cart.calculate_total()
        discounted_total = self.discount_policy.apply_loyalty_discount(total)
        expected_discounted_total = total * 0.90  # 10% loyalty discount
        self.assertAlmostEqual(discounted_total, expected_discounted_total, places=2)

    def test_order_and_invoice(self):
        """Test creating an order and generating an invoice."""
        self.cart.add_to_cart(self.ebook1)
        self.cart.add_to_cart(self.ebook2)
        order = Order(101, self.customer)
        order.cart = self.cart
        total = self.cart.calculate_total()
        discounted_total = self.discount_policy.apply_loyalty_discount(total)
        invoice = Invoice("INV-101", order, discounted_total)
        self.assertIn("INV-101", str(invoice))
        self.assertIn("Zayed", str(order))

if __name__ == "__main__":
    unittest.main()
