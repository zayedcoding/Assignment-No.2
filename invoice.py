class Invoice:
    """Represents an invoice for an order."""

    def __init__(self, invoice_id, order, amount_due):
        """Initialize an invoice with ID, order, and amount due."""
        self.__invoice_id = invoice_id  # Private attribute
        self.__order = order
        self.__amount_due = amount_due

    def __str__(self):
        """String representation of the invoice."""
        return f"Invoice ID: {self.__invoice_id}, Amount Due: ${self.__amount_due:.2f}"
