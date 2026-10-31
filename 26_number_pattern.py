rows = int(input("Enter number of rows: "))

for row in range(1, rows + 1):
    for number in range(1, row + 1):
        print(number, end=" ")
    print()
