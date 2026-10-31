terms = int(input("Enter number of terms: "))

if terms < 1:
    print("Enter a positive number of terms.")
else:
    a, b = 0, 1
    for _ in range(terms):
        print(a, end=" ")
        a, b = b, a + b
    print()
