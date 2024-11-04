class DiscountPolicy:
    """Applies various discounts to orders."""

    def __init__(self):
        """Initialize discount policy with default values."""
        self.__discount_type = None  # Private attribute
        self.__discount_value = 0.0

    def apply_loyalty_discount(self, amount):
        """Apply a loyalty discount to the amount."""
        self.__discount_type = "loyalty"
        self.__discount_value = 0.10
        return amount * (1 - self.__discount_value)

    def apply_bulk_discount(self, amount):
        """Apply a bulk purchase discount to the amount."""
        self.__discount_type = "bulk"
        self.__discount_value = 0.20
        return amount * (1 - self.__discount_value)

    def __str__(self):
        """String representation of the discount policy."""
        return f"Discount Type: {self.__discount_type}, Discount Value: {self.__discount_value * 100:.0f}%"
