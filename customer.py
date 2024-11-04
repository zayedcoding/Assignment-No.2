class Customer:
    """Represents a customer in the e-bookstore."""

    def __init__(self, customer_id, name, email, loyalty_member=False):
        """Initialize a Customer with ID, name, email, and loyalty status."""
        self.__customer_id = customer_id  # Private attribute
        self.__name = name
        self.__email = email
        self.__loyalty_member = loyalty_member

    # Getter and setter methods
    @property
    def name(self):
        """Get the customer's name."""
        return self.__name

    @name.setter
    def name(self, value):
        """Set the customer's name."""
        self.__name = value

    @property
    def email(self):
        """Get the customer's email."""
        return self.__email

    @loyalty_member.setter
    def loyalty_member(self, value):
        """Set the customer's loyalty status."""
        self.__loyalty_member = value

    def __str__(self):
        """String representation of the customer."""
        return f"Customer: {self.__name}, Loyalty Member: {self.__loyalty_member}"
