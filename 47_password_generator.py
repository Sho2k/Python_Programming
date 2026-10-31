import secrets
import string

length = int(input("Enter password length (minimum 8): "))

if length < 8:
    print("Choose a length of at least 8.")
else:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for _ in range(length))
    print("Generated password:", password)
