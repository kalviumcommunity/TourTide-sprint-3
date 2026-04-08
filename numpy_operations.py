"""
NumPy Mathematical Operations Demo
"""

import numpy as np


# ==============================
# 1. CREATE ARRAYS
# ==============================
def create_arrays():
    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([10, 20, 30, 40])

    return arr1, arr2


# ==============================
# 2. ELEMENT-WISE OPERATIONS
# ==============================
def array_operations(arr1, arr2):
    print("\n--- ARRAY OPERATIONS ---")

    print("Array 1:", arr1)
    print("Array 2:", arr2)

    print("Addition:", arr1 + arr2)
    print("Subtraction:", arr1 - arr2)
    print("Multiplication:", arr1 * arr2)
    print("Division:", arr1 / arr2)


# ==============================
# 3. SCALAR OPERATIONS
# ==============================
def scalar_operations(arr):
    print("\n--- SCALAR OPERATIONS ---")

    print("Original:", arr)
    print("Add 5:", arr + 5)
    print("Multiply by 2:", arr * 2)


# ==============================
# 4. LIST VS ARRAY COMPARISON
# ==============================
def list_vs_array():
    print("\n--- LIST vs ARRAY ---")

    list1 = [1, 2, 3]
    list2 = [4, 5, 6]

    print("List Addition:", list1 + list2)  # concatenation

    arr1 = np.array(list1)
    arr2 = np.array(list2)

    print("Array Addition:", arr1 + arr2)  # element-wise


# ==============================
# 5. MAIN
# ==============================
def main():
    arr1, arr2 = create_arrays()

    array_operations(arr1, arr2)
    scalar_operations(arr1)
    list_vs_array()


# ==============================
# ENTRY POINT
# ==============================
if __name__ == "__main__":
    main()