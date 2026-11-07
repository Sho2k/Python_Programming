"""Program 60: Linear Search"""

def linear_search(items, target):
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1

numbers = [12, 25, 7, 30, 18]
target = 30

position = linear_search(numbers, target)

if position != -1:
    print(f"{target} found at index {position}.")
else:
    print(f"{target} was not found.")
