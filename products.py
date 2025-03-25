class Product:
    """
    Represents a product in the e-commerce platform.
    """
    def __init__(self, product_id, name, description, price):
        """
        Initializes a new Product object.

        Args:
            product_id (int): The unique identifier for the product.
            name (str): The name of the product.
            description (str): A brief description of the product.
            price (float): The price of the product.
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name} (${self.price})"

# Sample products
products = [
    Product(1, "Laptop", "High-performance laptop", 1200.00),
    Product(2, "Mouse", "Wireless mouse", 25.00),
    Product(3, "Keyboard", "Mechanical keyboard", 75.00),
]

def get_product_by_id(product_id):
    """
    Retrieves a product from the list of products by its ID.

    Args:
        product_id (int): The ID of the product to retrieve.

    Returns:
        Product: The Product object with the given ID, or None if not found.
    """
    for product in products:
        if product.product_id == product_id:
            return product
    return None