"""Program 61: Binary Search"""

def binary_search(items, target):
    low = 0
    high = len(items) - 1

    while low <= high:
        middle = (low + high) // 2

        if items[middle] == target:
            return middle
        if items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return -1

numbers = [5, 10, 15, 20, 25, 30, 35]
target = 25

position = binary_search(numbers, target)

if position != -1:
    print(f"{target} found at index {position}.")
else:
    print(f"{target} was not found.")
