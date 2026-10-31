n = int(input("Enter a positive integer: "))

if n < 1:
    print("Please enter a positive integer.")
else:
    total = sum(range(1, n + 1))
    print("Sum:", total)
