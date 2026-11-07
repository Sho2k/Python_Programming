"""Program 64: Insertion Sort"""

def insertion_sort(items):
    result = items.copy()

    for index in range(1, len(result)):
        current = result[index]
        position = index - 1

        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1

        result[position + 1] = current

    return result

numbers = [9, 5, 1, 4, 3]
print("Original:", numbers)
print("Sorted:", insertion_sort(numbers))
