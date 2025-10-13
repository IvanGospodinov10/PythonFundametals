employees = input().split()
happiness_factor = int(input())

employees = list(map(lambda x: int(x) * happiness_factor,employees))
average_happiness = list(filter(lambda x: x >= sum(employees) / len(employees), employees))

if len(average_happiness) >= len(employees) / 2:
    print(f"Score: {len(average_happiness)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(average_happiness)}/{len(employees)}. Employees are not happy!")