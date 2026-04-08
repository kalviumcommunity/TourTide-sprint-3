import numpy as np


def create_arrays():
    list_1d = [1, 2, 3, 4, 5]
    arr1 = np.array(list_1d)

    list_2d = [[1, 2, 3], [4, 5, 6]]
    arr2 = np.array(list_2d)

    return arr1, arr2


def inspect(arr, name):
    print(f"\n{name}")
    print(arr)
    print("Shape:", arr.shape)
    print("Dimensions:", arr.ndim)
    print("Data Type:", arr.dtype)


def operations(arr):
    print("\nOperations:")
    print("Original:", arr)
    print("Add 10:", arr + 10)
    print("Multiply by 2:", arr * 2)


def main():
    arr1, arr2 = create_arrays()

    inspect(arr1, "1D Array")
    inspect(arr2, "2D Array")

    operations(arr1)


if __name__ == "__main__":
    main()