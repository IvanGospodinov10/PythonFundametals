student_dict = {}

command = input()
while ":" in command:
    info = command.split(":")

    student_name, student_id, student_course = info[0], info[1], info[2]
    if student_course not in student_dict:
        student_dict[student_course] = {}
    student_dict[student_course][student_id] = student_name
    # print(student_dict)
    command = input()

course = " ".join(command.split("_"))
for key,value in student_dict.items():
    if key == course:

        for student_id, student_name in value.items():
            print(f"{student_name} - {student_id}")

