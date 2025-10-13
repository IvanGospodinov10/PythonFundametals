rooms = int(input())

total_free_chair = 0
room_number = 0

for room in range(rooms):
    room_number += 1
    chairs_in_current_room, number_of_visitors = input().split()
    difference = len(chairs_in_current_room) - int(number_of_visitors)
    if difference < 0:
        print(f"{abs(difference)} more chairs needed in room {room_number}")
    total_free_chair += difference
if total_free_chair >= 0:
    print(f"Game On, {total_free_chair} free chairs left")