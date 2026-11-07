"""Program 49: Lambda Functions"""

square = lambda number: number ** 2
add = lambda first, second: first + second

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda number: number ** 2, numbers))

print("Square of 6:", square(6))
print("Sum of 10 and 20:", add(10, 20))
print("Squares:", squares)
