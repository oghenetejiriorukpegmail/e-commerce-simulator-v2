class ShoppingCart:
    """
    Represents a shopping cart for the e-commerce platform.
    """
    def __init__(self):
        """
        Initializes a new ShoppingCart object.
        """
        self.items = []

    def add_item(self, product, quantity=1):
        """
        Adds a product to the shopping cart.

        Args:
            product (Product): The product to add to the cart.
            quantity (int): The quantity of the product to add.
        """
        self.items.append({"product": product, "quantity": quantity})

    def remove_item(self, product):
        """
        Removes a product from the shopping cart.

        Args:
            product (Product): The product to remove from the cart.
        """
        self.items = [item for item in self.items if item["product"].product_id != product.product_id]

    def get_total(self):
        """
        Calculates the total price of the items in the cart.

        Returns:
            float: The total price of the items in the cart.
        """
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total

    def __str__(self):
        if not self.items:
            return "Your cart is empty."
        cart_str = "Your Cart:\n"
        for item in self.items:
            cart_str += f"- {item['product'].name} x {item['quantity']}\n"
        cart_str += f"Total: ${self.get_total()}"
        return cart_str