"""Program 57: JSON Handling"""

import json

student = {
    "name": "Anu",
    "age": 20,
    "course": "Computer Science",
    "marks": [85, 90, 88]
}

json_data = json.dumps(student, indent=4)
print("JSON data:")
print(json_data)

restored_student = json.loads(json_data)
print("Student name:", restored_student["name"])
print("Average marks:", sum(restored_student["marks"]) / len(restored_student["marks"]))
