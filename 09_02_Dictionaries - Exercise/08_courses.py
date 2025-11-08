courses = {}

while True:
    current_course = input()
    if current_course == "end":
        break
    course_name, student_name = current_course.split(" : ")
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)
for course, student in courses.items():
    print(f"{course}: {len(student)}")
    for name in student:
        print(f"-- {name}")