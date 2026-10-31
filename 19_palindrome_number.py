number = input("Enter a non-negative integer: ")

if number.isdigit() and number == number[::-1]:
    print("Palindrome number")
else:
    print("Not a palindrome number")
