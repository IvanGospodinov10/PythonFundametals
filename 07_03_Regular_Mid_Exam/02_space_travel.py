def travel(total_fuel: int, fuel_consumed: int) ->int:
    total_fuel -= fuel_consumed
    if total_fuel >= 0:
        print(f"The spaceship travelled {fuel_consumed} light-years.")
    return total_fuel


def enemy(total_amunition: int, enemy_armor: int) -> int:
    total_amunition -= enemy_armor
    print(f"An enemy with {enemy_armor} armour is defeated.")
    return total_amunition
    # elif total_fuel >= enemy_armor * 2:
    #     total_fuel -= enemy_armor * 2
    #     # result = total_fuel
    #     print(f"An enemy with {enemy_armor} armour is outmaneuvered.")
    #     return total_fuel
def run(total_fuel: int, enemy_armor: int) -> int:
    total_fuel -= enemy_armor * 2
    print(f"An enemy with {enemy_armor} armour is outmaneuvered.")
    return total_fuel


travel_route = input().split("||")
fuel = int(input())
ammunition = int(input())

for string in travel_route:
    command = string.split(" ")

    if command[0] == "Titan":
        print(f"You have reached Titan, all passengers are safe.")
        break
    if command[0] == "Travel":
        points = int(command[1])
        if fuel < points:
            print(f"Mission failed.")
            break
        fuel = travel(fuel, points)

    elif command[0] == "Enemy":
        points = int(command[1])
        if ammunition >= points:
            ammunition = enemy(ammunition, points)
        elif fuel >= points * 2:
            fuel = run(fuel, points)
        else:
            print(f"Mission failed.")
            break

    elif command[0] == "Repair":
        points = int(command[1])
        fuel += points
        ammunition += points * 2

        print(f"Ammunitions added: {points * 2}.")
        print(f"Fuel added: {points}.")


