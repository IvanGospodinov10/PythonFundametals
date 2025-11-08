lines = int(input())
students = {}

for line in range(lines):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
    students[name].append(grade)
for student, grades in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")