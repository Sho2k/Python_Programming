"""Program 50: map(), filter(), and reduce()"""

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

squares = list(map(lambda number: number ** 2, numbers))
evens = list(filter(lambda number: number % 2 == 0, numbers))
total = reduce(lambda first, second: first + second, numbers)

print("Numbers:", numbers)
print("Squares:", squares)
print("Even numbers:", evens)
print("Sum:", total)
