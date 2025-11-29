import re

participants = input().split(", ")

result = {name: 0 for name in participants}

name_pattern = r'[A-Za-z]'
distance_pattern = r'\d'

while True:
    line = input()
    if line == "end of race":
        break

    name = "".join(re.findall(name_pattern, line))
    distance = sum(int(digit) for digit in re.findall(distance_pattern, line))

    if name in result:
        result[name] += distance

sorted_result = sorted(result.items(), key = lambda x: x[1], reverse=True)
# print(sorted_result)
places = ["1st place:", "2nd place:", "3rd place:"]
for i in range(3):
    print(f"{places[i]} {sorted_result[i][0]}")
