import random

secret_number = random.randint(1, 20)
attempts = 0

print("Guess the number between 1 and 20.")

while True:
    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("Enter a whole number.")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low. Try again.")
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
