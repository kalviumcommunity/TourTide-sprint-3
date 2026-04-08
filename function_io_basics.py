"""
Function Input-Output Demo
(Passing data into functions and returning results)
"""

# ==============================
# 1. FUNCTION WITH PARAMETERS
# ==============================
def add(a, b):
    return a + b


# ==============================
# 2. FUNCTION RETURNING VALUE
# ==============================
def calculate_discount(price, discount_percent):
    discount = price * discount_percent / 100
    final_price = price - discount
    return final_price


# ==============================
# 3. USING RETURNED VALUES
# ==============================
def total_cost(price1, price2):
    total = add(price1, price2)   # using another function
    return total


# ==============================
# 4. FUNCTION CHAINING
# ==============================
def final_amount(price):
    discounted = calculate_discount(price, 10)
    total = total_cost(discounted, 50)  # adding extra fee
    return total


# ==============================
# 5. MAIN FUNCTION
# ==============================
def main():
    print("\n--- FUNCTION INPUT-OUTPUT DEMO ---")

    # Pass arguments
    result = add(5, 3)
    print("Sum:", result)

    # Return and reuse
    discounted_price = calculate_discount(1000, 20)
    print("Discounted Price:", discounted_price)

    # Using returned value in another function
    total = total_cost(200, 300)
    print("Total Cost:", total)

    # Chained function usage
    final = final_amount(500)
    print("Final Amount:", final)


# ==============================
# ENTRY POINT
# ==============================
if __name__ == "__main__":
    main()