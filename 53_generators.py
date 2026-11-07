"""Program 53: Generators"""

def countdown(start):
    while start > 0:
        yield start
        start -= 1

def even_numbers(limit):
    for number in range(2, limit + 1, 2):
        yield number

print("Countdown:")
for value in countdown(5):
    print(value, end=" ")

print("\nEven numbers:")
print(list(even_numbers(10)))
