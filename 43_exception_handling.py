try:
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))
    print("Result:", first / second)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter valid numbers.")
finally:
    print("Program completed.")
