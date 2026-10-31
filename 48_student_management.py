students = {}

def add_student():
    roll = input("Enter roll number: ").strip()
    name = input("Enter student name: ").strip()

    if not roll or not name:
        print("Roll number and name cannot be empty.")
    elif roll in students:
        print("That roll number already exists.")
    else:
        students[roll] = name
        print("Student added.")

def view_students():
    if not students:
        print("No student records found.")
        return

    print("\nStudent Records")
    for roll, name in students.items():
        print(f"Roll: {roll} | Name: {name}")

while True:
    print("\n1. Add student")
    print("2. View students")
    print("3. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
