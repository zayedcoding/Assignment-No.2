class Order:
    """Represents an order made by a customer."""

    def __init__(self, order_id, customer):
        """Initialize an order with a unique ID and associated customer."""
        self.__order_id = order_id  # Private attribute
        self.__customer = customer
        self.cart = ShoppingCart()  # Composition

    def place_order(self):
        """Simulate placing the order."""
        return f"Order {self.__order_id} placed for {self.__customer.name}."

    def __str__(self):
        """String representation of the order."""
        return f"Order ID: {self.__order_id}, Customer: {self.__customer.name}\n" + str(self.cart)
