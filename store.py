class Store:
    """Represents a store that manages a list of products."""

    def __init__(self, product_list):
        """Create a store with an initial list of Product objects."""

        # The Store object keeps references to all Product objects in
        # one list. This is the composition between Store and Product:
        # a Store "has" multiple products.
        self.products = product_list

    def add_product(self, product):
        """Add a Product object to the store."""

        # The complete Product object is added to the store's product
        # list. Its name, price, quantity, and active status remain
        # managed by the Product class.
        self.products.append(product)

    def remove_product(self, product):
        """Remove a Product object from the store."""

        # Remove the specified Product object from the store's list.
        # If the object is not contained in the list, Python raises
        # a ValueError automatically.
        self.products.remove(product)

    def get_total_quantity(self):
        """Return the total stock quantity of all products."""

        total_quantity = 0

        # Ask each Product object for its current quantity by calling
        # the Product.get_quantity() method. The Store then adds the
        # individual quantities together.
        for product in self.products:
            total_quantity += product.get_quantity()

        return total_quantity

    def get_all_products(self):
        """Return a list containing all active Product objects."""

        active_products = []

        # Product.is_active() decides whether a product is currently
        # available. Products that have been deactivated, for example
        # because their quantity reached zero, are not added.
        for product in self.products:
            if product.is_active():
                active_products.append(product)

        return active_products

    def order(self, shopping_list):
        """Buy all requested products and return the total order price."""

        total_price = 0

        # Each tuple in the shopping list contains:
        # (Product object, requested quantity)
        #
        # Product.buy() checks whether the purchase is possible,
        # reduces the product's stock, deactivates it when necessary,
        # and returns the price for that part of the order.
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price
