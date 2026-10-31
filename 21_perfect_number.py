number = int(input("Enter a positive integer: "))

if number <= 0:
    print("Enter a positive integer.")
else:
    divisor_sum = sum(i for i in range(1, number) if number % i == 0)
    print("Perfect number" if divisor_sum == number else "Not a perfect number")
