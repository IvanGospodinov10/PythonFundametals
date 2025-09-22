lost_fights = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

# expenses = 0

total_helmet_price = lost_fights // 2
total_sword_price = lost_fights // 3
total_shield_price = lost_fights // (2 * 3)
total_armor_price = total_shield_price // 2

expenses = ((total_helmet_price * helmet_price)
            + (total_sword_price * sword_price)
            + (total_shield_price * shield_price)
            + (total_armor_price * armor_price))


print(f"Gladiator expenses: {expenses:.2f} aureus")