"""
Conditional Statements Demo
"""

# ==============================
# 1. BASIC IF
# ==============================
def basic_if():
    print("\n--- BASIC IF ---")

    age = 18

    if age >= 18:
        print("Eligible to vote")


# ==============================
# 2. IF-ELSE
# ==============================
def if_else():
    print("\n--- IF ELSE ---")

    temperature = 30

    if temperature > 25:
        print("It's hot")
    else:
        print("It's cool")


# ==============================
# 3. IF-ELIF-ELSE
# ==============================
def multiple_conditions():
    print("\n--- IF ELIF ELSE ---")

    score = 75

    if score >= 90:
        print("Grade: A")
    elif score >= 70:
        print("Grade: B")
    elif score >= 50:
        print("Grade: C")
    else:
        print("Fail")


# ==============================
# 4. LOGICAL OPERATORS
# ==============================
def logical_operators():
    print("\n--- LOGICAL OPERATORS ---")

    age = 25
    has_id = True

    # AND
    if age >= 18 and has_id:
        print("Allowed entry")

    # OR
    is_weekend = False
    if is_weekend or age > 21:
        print("Special access granted")

    # NOT
    is_banned = False
    if not is_banned:
        print("User is allowed")


# ==============================
# 5. STRING CONDITIONS
# ==============================
def string_conditions():
    print("\n--- STRING CONDITIONS ---")

    role = "admin"

    if role == "admin":
        print("Full access")
    elif role == "user":
        print("Limited access")
    else:
        print("Guest access")


# ==============================
# 6. MAIN
# ==============================
def main():
    basic_if()
    if_else()
    multiple_conditions()
    logical_operators()
    string_conditions()


# ==============================
# 7. ENTRY POINT
# ==============================
if __name__ == "__main__":
    main()