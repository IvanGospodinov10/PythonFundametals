number_of_wagons = int(input())
wagons = [0] * number_of_wagons

while True:
    command_text = input()

    if command_text == "End":
        break
    parts = command_text.split()
    command = parts[0]
    if command == "add":
        wagons[-1] += int(parts[1])
    elif command == "insert":
        wagons[int(parts[1])] += int(parts[2])
    elif command == "leave":
        wagons[int(parts[1])] -= int(parts[2])

print(wagons)


