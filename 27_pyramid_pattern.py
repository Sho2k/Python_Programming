rows = int(input("Enter number of rows: "))

for row in range(1, rows + 1):
    spaces = " " * (rows - row)
    stars = "* " * row
    print(spaces + stars)
