def main():
    """Main function to demonstrate the e-bookstore system functionality."""

    # Create EBook instances
    ebook1 = EBook("Python Basics", "John Doe", "2021-01-01", "Programming", 29.99, "ISBN12345")
    ebook2 = EBook("Advanced Python", "Jane Smith", "2022-02-01", "Programming", 39.99, "ISBN67890")

    # Create and display Catalog
    catalog = Catalog()
    catalog.add_ebook(ebook1)
    catalog.add_ebook(ebook2)
    print(catalog)

    # Create Customer instance
    customer = Customer(1, "Alice", "alice@example.com", True)
    print(customer)

    # Create ShoppingCart and add items
    cart = ShoppingCart()
    cart.add_to_cart(ebook1)
    cart.add_to_cart(ebook2)
    print(cart)

    # Create Order
    order = Order(101, customer)
    order.cart = cart
    print(order)

    # Apply Discount
    discount_policy = DiscountPolicy()
    discounted_total = discount_policy.apply_loyalty_discount(cart.calculate_total())
    print(f"Total after discount: ${discounted_total:.2f}")

    # Create and display Invoice
    invoice = Invoice("INV-101", order, discounted_total)
    print(invoice)

if __name__ == "__main__":
    main()
