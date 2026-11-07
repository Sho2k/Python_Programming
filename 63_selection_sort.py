"""Program 63: Selection Sort"""

def selection_sort(items):
    result = items.copy()

    for start in range(len(result)):
        minimum_index = start
        for index in range(start + 1, len(result)):
            if result[index] < result[minimum_index]:
                minimum_index = index
        result[start], result[minimum_index] = result[minimum_index], result[start]

    return result

numbers = [29, 10, 14, 37, 13]
print("Original:", numbers)
print("Sorted:", selection_sort(numbers))
