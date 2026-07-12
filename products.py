class Product:
    """Represents a product that is available in the store."""

    def __init__(self, name, price, quantity):
        """Create a product with a name, price, and stock quantity."""

        # Every product must have a non-empty name.
        if not name.strip():
            raise ValueError("Product name cannot be empty.")

        # A product price cannot be negative.
        if price < 0:
            raise ValueError("Product price cannot be negative.")

        # The initial stock quantity cannot be negative.
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")

        # Store the product information as instance variables.
        self.name = name
        self.price = price
        self.quantity = quantity

        # A newly created product is active by default.
        self.active = True

    def get_quantity(self):
        """Return the current stock quantity."""
        return self.quantity

    def set_quantity(self, quantity):
        """Set a new stock quantity for the product."""

        # Prevent the product from having a negative stock quantity.
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")

        self.quantity = quantity

        # Products with no remaining stock are no longer available.
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """Return True when the product is active."""
        return self.active

    def activate(self):
        """Mark the product as active."""
        self.active = True

    def deactivate(self):
        """Mark the product as inactive."""
        self.active = False

    def show(self):
        """Display the product information in the console."""
        print(
            f"{self.name}, Price: ${self.price}, "
            f"Quantity: {self.quantity}"
        )

    def buy(self, quantity):
        """Buy a quantity of the product and return the total price."""

        # A customer must buy at least one item.
        if quantity <= 0:
            raise ValueError(
                "Purchase quantity must be greater than zero."
            )

        # Inactive products cannot be purchased.
        if not self.active:
            raise ValueError("Product is not active.")

        # The requested amount cannot exceed the available stock.
        if quantity > self.quantity:
            raise ValueError("Not enough items in stock.")

        # Calculate the stock quantity remaining after the purchase.
        remaining_quantity = self.quantity - quantity

        # The setter also deactivates the product when stock reaches zero.
        self.set_quantity(remaining_quantity)

        # Return the complete price of this purchase.
        return self.price * quantity
