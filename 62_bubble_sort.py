"""Program 62: Bubble Sort"""

def bubble_sort(items):
    result = items.copy()
    size = len(result)

    for end in range(size - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if not swapped:
            break

    return result

numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original:", numbers)
print("Sorted:", bubble_sort(numbers))
