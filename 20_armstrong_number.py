number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Armstrong check here expects a non-negative integer.")
else:
    digits = str(number)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    print("Armstrong number" if total == number else "Not an Armstrong number")
