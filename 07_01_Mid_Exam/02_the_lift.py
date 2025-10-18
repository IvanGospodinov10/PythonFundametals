people_in_queue = int(input())
lift_wagons = list(map(int, input().split()))

wagon_capacity = 4
for i in range(len(lift_wagons)):
    people_left = 0
    if lift_wagons[i] == 4:
        continue
    elif people_in_queue + lift_wagons[i] <= 4:
        lift_wagons[i] += people_in_queue
        people_left = people_in_queue
    else:
        people_left = wagon_capacity - lift_wagons[i]
        lift_wagons[i] = people_left + lift_wagons[i]
    people_in_queue -= people_left
if people_in_queue <= 0:
    print(f"The lift has empty spots!")
    print(" ".join(str(num) for num in lift_wagons))
else:
    print(f"There isn't enough space! {people_in_queue} people in a queue!")
    print(" ".join(str(num) for num in lift_wagons))