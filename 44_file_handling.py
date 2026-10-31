file_name = "sample.txt"

with open(file_name, "w", encoding="utf-8") as file:
    file.write("Welcome to Python file handling!")

with open(file_name, "r", encoding="utf-8") as file:
    content = file.read()

print(content)
