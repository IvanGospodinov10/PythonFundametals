employee_one = int(input())
employee_two = int(input())
employee_tree = int(input())
students_in_queue = int(input())

efficiency  = employee_one + employee_two + employee_tree
hours = 0

while students_in_queue > 0:
    hours += 1

    if hours % 4 == 0:
        # hours += 1
        continue
    students_in_queue -= efficiency
print(f"Time needed: {hours}h.")
