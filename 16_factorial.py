n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for number in range(1, n + 1):
        factorial *= number
    print("Factorial:", factorial)
