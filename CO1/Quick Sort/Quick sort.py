

# Product list
products = [
    ("Laptop", 55000),
    ("Headphones", 2000),
    ("Keyboard", 1200),
    ("Mobile", 25000),
    ("Mouse", 800)
]


# ------------------------------------------
# Quick Sort Function
# ------------------------------------------
def quick_sort(products):

    # Base condition
    if len(products) <= 1:
        return products

    # Select the last product as pivot
    pivot = products[-1]

    left = []
    right = []

    # Compare prices with pivot
    for product in products[:-1]:

        if product[1] <= pivot[1]:
            left.append(product)
        else:
            right.append(product)

    # Recursively sort left and right
    return quick_sort(left) + [pivot] + quick_sort(right)


# ------------------------------------------
# Sort Products
# ------------------------------------------
sorted_products = quick_sort(products)


# ------------------------------------------
# Display Result
# ------------------------------------------
print("Products Sorted by Price")
print("-------------------------")

for name, price in sorted_products:
    print(f"{name} - ₹{price}")
