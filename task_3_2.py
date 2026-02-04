students = [
    {"name": "Mosab", "grades": [75, 90, 85]},
    {"name": "Ricky", "grades": [95, 91, 80]},
    {"name": "Omar", "grades": [91, 95, 99]}
]

for student in students:
    average = sum(student["grades"]) / 3
    print(f"Student: {student["name"]}, Average Grade: {average}")
