# ==========================================
#        ONLINE SHOPPING CART
# ==========================================

# Product catalog
products = {
    1: {"name": "Laptop", "price": 55000},
    2: {"name": "Smartphone", "price": 25000},
    3: {"name": "Headphones", "price": 2000},
    4: {"name": "Keyboard", "price": 1200},
    5: {"name": "Mouse", "price": 800},
    6: {"name": "Smart Watch", "price": 3500},
    7: {"name": "Power Bank", "price": 1500},
    8: {"name": "USB Cable", "price": 500}
}

# Shopping cart
cart = {}


# ------------------------------------------
# Display Products
# ------------------------------------------
def display_products():

    print("\n========== PRODUCT CATALOG ==========")

    print(f"{'ID':<5}{'Product':<20}{'Price':>10}")
    print("-" * 40)

    for product_id, product in products.items():
        print(
            f"{product_id:<5}"
            f"{product['name']:<20}"
            f"₹{product['price']:>8}"
        )

    print("-" * 40)


# ------------------------------------------
# Add Product to Cart
# ------------------------------------------
def add_to_cart():

    display_products()

    try:
        product_id = int(input("\nEnter Product ID: "))

        if product_id not in products:
            print("Invalid Product ID!")
            return

        quantity = int(input("Enter Quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        if product_id in cart:
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity

        print(
            f"{products[product_id]['name']} "
            f"added to cart successfully!"
        )

    except ValueError:
        print("Please enter a valid number.")


# ------------------------------------------
# View Cart
# ------------------------------------------
def view_cart():

    print("\n========== SHOPPING CART ==========")

    if not cart:
        print("Your cart is empty.")
        return

    total = 0

    print(
        f"{'Product':<20}"
        f"{'Qty':<8}"
        f"{'Price':<12}"
        f"{'Subtotal':<12}"
    )

    print("-" * 55)

    for product_id, quantity in cart.items():

        product = products[product_id]

        subtotal = product["price"] * quantity

        total += subtotal

        print(
            f"{product['name']:<20}"
            f"{quantity:<8}"
            f"₹{product['price']:<11}"
            f"₹{subtotal:<11}"
        )

    print("-" * 55)
    print(f"{'Total Amount':<40} ₹{total}")


# ------------------------------------------
# Remove Product from Cart
# ------------------------------------------
def remove_from_cart():

    if not cart:
        print("\nYour cart is empty.")
        return

    view_cart()

    try:
        product_id = int(
            input("\nEnter Product ID to remove: ")
        )

        if product_id not in cart:
            print("Product is not in your cart.")
            return

        quantity = int(
            input("Enter quantity to remove: ")
        )

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        if quantity >= cart[product_id]:

            del cart[product_id]

            print("Product removed from cart.")

        else:

            cart[product_id] -= quantity

            print("Quantity updated successfully.")

    except ValueError:
        print("Please enter a valid number.")


# ------------------------------------------
# Calculate Total
# ------------------------------------------
def calculate_total():

    total = 0

    for product_id, quantity in cart.items():

        total += (
            products[product_id]["price"]
            * quantity
        )

    return total


# ------------------------------------------
# Checkout
# ------------------------------------------
def checkout():

    if not cart:
        print("\nYour cart is empty.")
        return

    print("\n========== CHECKOUT ==========")

    total = calculate_total()

    print("Cart Total      : ₹", total)

    # Discount
    if total >= 50000:
        discount = total * 0.10
    elif total >= 20000:
        discount = total * 0.05
    else:
        discount = 0

    # GST
    amount_after_discount = total - discount

    gst = amount_after_discount * 0.18

    final_amount = (
        amount_after_discount + gst
    )

    print("Discount        : ₹", round(discount, 2))
    print("GST (18%)       : ₹", round(gst, 2))
    print("-" * 35)
    print("Final Amount    : ₹", round(final_amount, 2))

    print("\nThank you for shopping with us!")

    # Empty cart after successful checkout
    cart.clear()


# ------------------------------------------
# Main Menu
# ------------------------------------------
def main():

    while True:

        print("\n")
        print("==========================================")
        print("        ONLINE SHOPPING CART")
        print("==========================================")

        print("1. View Products")
        print("2. Add Product to Cart")
        print("3. View Shopping Cart")
        print("4. Remove Product from Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            display_products()

        elif choice == "2":

            add_to_cart()

        elif choice == "3":

            view_cart()

        elif choice == "4":

            remove_from_cart()

        elif choice == "5":

            checkout()

        elif choice == "6":

            print("\nThank you for using Online Shopping Cart!")
            break

        else:

            print("\nInvalid choice! Please try again.")


# ------------------------------------------
# Start Program
# ------------------------------------------
if __name__ == "__main__":
    main()
