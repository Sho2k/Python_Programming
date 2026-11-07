"""Program 59: List Operations (Array Basics)"""

numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)

numbers.append(60)
print("After append:", numbers)

numbers.insert(2, 25)
print("After insert:", numbers)

numbers.remove(40)
print("After remove:", numbers)

print("Element at index 1:", numbers[1])
print("Length:", len(numbers))
