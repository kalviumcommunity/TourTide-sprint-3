"""
Loops Demo - for and while loops
"""

# ==============================
# 1. FOR LOOP (RANGE)
# ==============================
def for_range():
    print("\n--- FOR LOOP (RANGE) ---")

    for i in range(1, 6):
        print("Number:", i)


# ==============================
# 2. FOR LOOP (LIST)
# ==============================
def for_list():
    print("\n--- FOR LOOP (LIST) ---")

    fruits = ["apple", "banana", "cherry"]

    for fruit in fruits:
        print("Fruit:", fruit)


# ==============================
# 3. WHILE LOOP
# ==============================
def while_loop():
    print("\n--- WHILE LOOP ---")

    count = 1

    while count <= 5:
        print("Count:", count)
        count += 1   # IMPORTANT (prevents infinite loop)


# ==============================
# 4. BREAK AND CONTINUE
# ==============================
def loop_control():
    print("\n--- BREAK & CONTINUE ---")

    for i in range(1, 6):

        if i == 3:
            print("Skipping 3")
            continue

        if i == 5:
            print("Stopping at 5")
            break

        print("Value:", i)


# ==============================
# 5. MAIN
# ==============================
def main():
    for_range()
    for_list()
    while_loop()
    loop_control()


# ==============================
# 6. ENTRY POINT
# ==============================
if __name__ == "__main__":
    main()