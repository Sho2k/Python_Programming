number = int(input("Enter an integer: "))

if number <= 1:
    print("Not a prime number")
else:
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
