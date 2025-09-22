number_of_lines = int(input())

water_total = 0
for number in range(1, number_of_lines + 1):
    liters_of_water = int(input())

    if liters_of_water + water_total > 255:
        print(f"Insufficient capacity!")
        continue
    water_total += liters_of_water
print(f"{water_total}")