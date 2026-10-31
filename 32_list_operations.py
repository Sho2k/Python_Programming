numbers = [10, 20, 30, 40, 50]
print("Original:", numbers)

numbers.append(60)
print("After append:", numbers)

numbers.remove(30)
print("After remove:", numbers)

numbers.sort()
print("Sorted:", numbers)
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Length:", len(numbers))
