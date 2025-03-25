from products import products, get_product_by_id
from cart import ShoppingCart
from checkout import checkout

def main():
    """
    Main function to simulate the e-commerce platform.
    """
    print("Welcome to the E-commerce Simulator!")

    # Display available products
    print("\nAvailable Products:")
    for product in products:
        print(f"- {product}")

    # Create a shopping cart
    cart = ShoppingCart()

    # Add products to the cart
    product1 = get_product_by_id(1)
    product2 = get_product_by_id(2)

    if product1:
        cart.add_item(product1, 2)
    if product2:
        cart.add_item(product2)

    # Display the cart
    print(f"\n{cart}")

    # Checkout
    if checkout(cart):
        print("\nThank you for your order!")
    else:
        print("\nCheckout failed.")

if __name__ == "__main__":
    main()