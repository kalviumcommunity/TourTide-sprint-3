"""
Working with Lists, Tuples, and Dictionaries
"""

# ==============================
# 1. LIST (Mutable)
# ==============================
def list_demo():
    print("\n--- LIST DEMO ---")

    fruits = ["apple", "banana", "cherry"]
    print("Original list:", fruits)

    # Access
    print("First fruit:", fruits[0])

    # Modify
    fruits[1] = "orange"
    print("Modified list:", fruits)

    # Add
    fruits.append("grape")
    print("After adding:", fruits)

    # Remove
    fruits.remove("apple")
    print("After removing:", fruits)


# ==============================
# 2. TUPLE (Immutable)
# ==============================
def tuple_demo():
    print("\n--- TUPLE DEMO ---")

    colors = ("red", "green", "blue")
    print("Tuple:", colors)

    # Access
    print("First color:", colors[0])

    # Try modifying (will fail)
    try:
        colors[1] = "yellow"
    except TypeError as e:
        print("Error (tuples are immutable):", e)


# ==============================
# 3. DICTIONARY (Key-Value)
# ==============================
def dict_demo():
    print("\n--- DICTIONARY DEMO ---")

    student = {
        "name": "Lizz",
        "age": 20,
        "course": "Software Engineering"
    }

    print("Original dictionary:", student)

    # Access
    print("Name:", student["name"])

    # Modify
    student["age"] = 21
    print("Updated age:", student)

    # Add new key
    student["grade"] = "A"
    print("After adding grade:", student)

    # Remove key
    student.pop("course")
    print("After removing course:", student)


# ==============================
# 4. MAIN FUNCTION
# ==============================
def main():
    list_demo()
    tuple_demo()
    dict_demo()


# ==============================
# 5. ENTRY POINT
# ==============================
if __name__ == "__main__":
    main()