fires_with_cells = input().split("#")
# print(fires_with_cells)
water = int(input())

effort = 0
cells = []

for fire_cell in fires_with_cells:
    fire_type, level = fire_cell.split(" = ")
    if fire_type == "High":
        if 81 <= int(level) <= 125:
            if water - int(level) >= 0:
                water -= int(level)
                effort += int(level) * 0.25
                cells.append(int(level))
    elif fire_type == "Medium":
        if 51 <= int(level) <= 80:
            if water - int(level) >= 0:
                water -= int(level)
                effort += int(level) * 0.25
                cells.append(int(level))
    elif fire_type == "Low":
        if 1 <= int(level) <= 50:
            if water - int(level) >= 0:
                water -= int(level)
                effort += int(level) * 0.25
                cells.append(int(level))

total_fire = sum(cells)
print("Cells:")
for num in cells:
    print(f" - {num}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
