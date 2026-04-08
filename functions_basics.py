"""
Functions Demo - Defining and Calling Functions
"""

# ==============================
# 1. SIMPLE FUNCTION
# ==============================
def greet():
    print("Hello! Welcome to Python functions.")


# ==============================
# 2. FUNCTION WITH PARAMETERS
# ==============================
def add_numbers(a, b):
    result = a + b
    return result


# ==============================
# 3. FUNCTION WITH LOGIC
# ==============================
def check_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# ==============================
# 4. FUNCTION WITH MULTIPLE STEPS
# ==============================
def calculate_total(price, quantity):
    total = price * quantity
    return total


# ==============================
# 5. SCOPE DEMO
# ==============================
def scope_example():
    local_var = "I am inside function"
    print(local_var)


# ==============================
# 6. MAIN FUNCTION
# ==============================
def main():
    print("\n--- FUNCTION DEMO ---")

    # Call simple function
    greet()

    # Call function with arguments
    sum_result = add_numbers(5, 3)
    print("Sum:", sum_result)

    # Call function with condition logic
    print("Number is:", check_even(10))

    # Call function with calculation
    total = calculate_total(100, 2)
    print("Total:", total)

    # Scope demo
    scope_example()

    # Trying to access local variable (will fail if uncommented)
    # print(local_var)


# ==============================
# 7. ENTRY POINT
# ==============================
if __name__ == "__main__":
    main()