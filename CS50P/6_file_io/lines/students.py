students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")
        student = {"name":name, "house":house}
        students.append(student)

# def get_name(student):
#     return student["name"]

# for student in sorted(students):
#     print(student)
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")

