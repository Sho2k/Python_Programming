number = abs(int(input("Enter an integer: ")))
digit_sum = sum(int(digit) for digit in str(number))
print("Sum of digits:", digit_sum)
