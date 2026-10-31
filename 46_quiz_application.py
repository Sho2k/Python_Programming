questions = [
    ("Which keyword defines a function in Python?", "def"),
    ("Which data type stores True or False?", "bool"),
    ("Which symbol starts a comment?", "#"),
]

score = 0

for question, answer in questions:
    print("\n" + question)
    user_answer = input("Your answer: ").strip()

    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Correct answer:", answer)

print(f"\nYour score: {score}/{len(questions)}")
