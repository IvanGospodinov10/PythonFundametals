group_size = int(input())
days = int(input())

coins = 0

for num_of_days in range(1, days + 1):

    if num_of_days % 10 == 0:
        group_size -= 2
    if num_of_days % 15 == 0:
        group_size += 5

    if num_of_days % 3 == 0:
        coins -= group_size * 3
    if num_of_days % 5 == 0:
        coins += group_size * 20
        if num_of_days % 3 == 0:
            coins -= group_size * 2


    coins += 50
    coins -= group_size * 2

coins_per_companion = coins // group_size
print(f"{group_size} companions received {coins_per_companion} coins each.")