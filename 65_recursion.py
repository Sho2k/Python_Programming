"""Program 65: Recursion"""

def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if number in (0, 1):
        return 1
    return number * factorial(number - 1)

def fibonacci(position):
    if position < 0:
        raise ValueError("Position cannot be negative.")
    if position <= 1:
        return position
    return fibonacci(position - 1) + fibonacci(position - 2)

value = 5
print(f"Factorial of {value}:", factorial(value))
print("First 8 Fibonacci numbers:", [fibonacci(index) for index in range(8)])
