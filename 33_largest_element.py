numbers = [10, 45, 23, 89, 12]

if numbers:
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    print("Largest element:", largest)
else:
    print("The list is empty.")
