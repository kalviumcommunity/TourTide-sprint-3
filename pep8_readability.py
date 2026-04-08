"""
PEP 8 Readability Demo
Good variable naming and meaningful comments
"""

# ==============================
# BAD EXAMPLE (DON'T DO THIS)
# ==============================
def bad_example():
    print("\n--- BAD EXAMPLE ---")

    x = 1000
    y = 20

    # subtract discount
    z = x - (x * y / 100)

    print("Result:", z)


# ==============================
# GOOD EXAMPLE (PEP 8)
# ==============================
def good_example():
    print("\n--- GOOD EXAMPLE ---")

    original_price = 1000
    discount_percentage = 20

    # Calculate final price after applying discount
    discount_amount = original_price * discount_percentage / 100
    final_price = original_price - discount_amount

    print("Final Price:", final_price)


# ==============================
# ANOTHER CLEAN FUNCTION
# ==============================
def calculate_total_cost(price_per_item, quantity):
    """
    Calculate total cost based on price and quantity.
    """
    total_cost = price_per_item * quantity
    return total_cost


# ==============================
# MAIN FUNCTION
# ==============================
def main():
    bad_example()
    good_example()

    total = calculate_total_cost(100, 3)
    print("\nTotal Cost:", total)


# ==============================
# ENTRY POINT
# ==============================
if __name__ == "__main__":
    main()