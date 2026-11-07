"""Program 51: List Comprehension"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [number ** 2 for number in numbers]
evens = [number for number in numbers if number % 2 == 0]
labels = ["Even" if number % 2 == 0 else "Odd" for number in numbers]

print("Squares:", squares)
print("Even numbers:", evens)
print("Number types:", labels)
