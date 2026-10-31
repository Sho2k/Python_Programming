def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if number <= 1:
        return 1
    return number * factorial(number - 1)

value = int(input("Enter a non-negative integer: "))

try:
    print("Factorial:", factorial(value))
except ValueError as error:
    print(error)
