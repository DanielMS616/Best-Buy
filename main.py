import products
import store


def display_products(store_object):
    """Display all active products and return them as a list."""

    # Store.get_all_products() returns a new list containing only
    # Product objects whose active status is currently True.
    # Products with quantity 0 have been deactivated and are omitted.
    active_products = store_object.get_all_products()

    print("------")

    # enumerate() goes through active_products and returns two values
    # in each loop: product_number is the visible number, starting at 1,
    # and product is the current Product object from the list.
    for product_number, product in enumerate(active_products, start=1):
        print(f"{product_number}. ", end="")
        product.show()

    print("------")

    # Return the same list so the displayed product numbers can later
    # be connected to the correct Product objects during an order.
    return active_products


def make_order(store_object):
    """Collect a shopping list and place the completed order."""

    # Display all active products and keep the returned list.
    active_products = display_products(store_object)

    # If all products are inactive, there is nothing the user can buy.
    if len(active_products) == 0:
        print("No active products are available.")
        return

    # Store each selected Product object together with its requested
    # quantity. Store.order() expects a list containing these tuples:
    # [(Product object, quantity), ...]
    shopping_list = []

    print("When you want to finish order, enter empty text.")

    # Allow the user to add several products before completing and
    # processing the complete order.
    while True:
        product_number_text = input(
            "Which product # do you want? "
        )
        quantity_text = input(
            "What amount do you want? "
        )

        # An empty product number finishes the current shopping list.
        if product_number_text == "":
            break

        try:
            # Convert both entries into integers. They are then used as
            # the product number and the requested purchase quantity.
            product_number = int(product_number_text)
            quantity = int(quantity_text)

        except ValueError:
            # int() raises ValueError when the user enters letters,
            # decimal numbers, or an empty quantity.
            print("Please enter valid whole numbers.")
            print()
            continue

        # The visible product numbers begin at 1. A valid number must
        # therefore be between 1 and the number of active products.
        if (
            product_number < 1
            or product_number > len(active_products)
        ):
            print("This product number does not exist.")
            print()
            continue

        # Product.buy() accepts only quantities greater than zero.
        if quantity <= 0:
            print("The amount must be greater than zero.")
            print()
            continue

        # The menu shows product numbers starting at 1, while Python
        # list indexes start at 0. Subtract 1 to convert the user's
        # product number into the matching active_products position.
        product_index = product_number - 1
        selected_product = active_products[product_index]

        # A Product object can be selected more than once before the
        # order is completed. Add quantities already requested for
        # this object so the combined amount can be checked.
        quantity_already_requested = 0

        for product, requested_quantity in shopping_list:
            if product == selected_product:
                quantity_already_requested += requested_quantity

        complete_requested_quantity = (
            quantity_already_requested + quantity
        )

        # Compare the complete requested quantity with the current
        # product stock. This prevents Store.order() from processing
        # part of the order before a later purchase fails.
        if (
            complete_requested_quantity
            > selected_product.get_quantity()
        ):
            print("Not enough items in stock.")
            print()
            continue

        # Add a tuple containing the selected Product object and the
        # requested quantity. Store.order() processes every tuple later.
        shopping_list.append(
            (selected_product, quantity)
        )

        print("Product added to list!")
        print()

    # Do not call Store.order() when the user finishes without adding
    # a Product object to the shopping list.
    if len(shopping_list) == 0:
        print("No products were selected.")
        return

    try:
        # Store.order() loops through the shopping list and calls
        # Product.buy() for each tuple. Product.buy() checks the stock,
        # reduces the quantity, and returns the individual price.
        total_payment = store_object.order(shopping_list)

        print("********")
        print(f"Order made! Total payment: ${total_payment}")

    except ValueError as error:
        # The inputs were already checked above. This exception handler
        # still prevents an unexpected Product.buy() error from ending
        # the complete store program.
        print(f"Order could not be completed: {error}")


def start(store_object):
    """Run the store menu until the user chooses to quit."""

    while True:
        print()
        print("   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        menu_choice = input("Please choose a number: ")

        if menu_choice == "1":
            # display_products() gets all active Product objects from
            # Store and calls Product.show() for every object.
            display_products(store_object)

        elif menu_choice == "2":
            # Store.get_total_quantity() asks every Product object for
            # its quantity and returns the sum of all quantities.
            total_quantity = store_object.get_total_quantity()

            print(f"Total of {total_quantity} items in store")

        elif menu_choice == "3":
            # make_order() creates a shopping list and passes it to
            # Store.order(), which processes the Product objects.
            make_order(store_object)

        elif menu_choice == "4":
            # break ends the menu loop and therefore the program.
            break

        else:
            # Only the menu options 1, 2, 3, and 4 are valid.
            print(
                "Invalid choice. "
                "Please choose a number from 1 to 4."
            )


def main():
    """Create the initial inventory and start the store program."""

    # Create the Product objects for the initial store inventory.
    product_list = [
        products.Product(
            "MacBook Air M2",
            price=1450,
            quantity=100
        ),
        products.Product(
            "Bose QuietComfort Earbuds",
            price=250,
            quantity=500
        ),
        products.Product(
            "Google Pixel 7",
            price=500,
            quantity=250
        )
    ]

    # Pass the list of Product objects to the Store constructor.
    best_buy = store.Store(product_list)

    # Pass the completed Store object to the user interface.
    start(best_buy)


if __name__ == "__main__":
    main()
