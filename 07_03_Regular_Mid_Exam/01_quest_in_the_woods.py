days_of_the_quest = int(input())
group_number = int(input())
total_energy = float(input())
water_per_person = float(input())
food_per_person = float(input())

total_water_need = days_of_the_quest * water_per_person * group_number
total_food_need = days_of_the_quest * food_per_person * group_number

for current_day in range(1, days_of_the_quest + 1):
    daily_activity = float(input())

    total_energy -= daily_activity
    # total_food_need -= food_per_person * group_number
    # total_water_need -= water_per_person * group_number
    if total_energy <= 0:
        break

    if current_day % 2 == 0:
        total_energy += total_energy * 0.05
        total_water_need -= total_water_need * 0.30
    if current_day % 3 == 0:
        total_energy += total_energy * 0.10
        total_food_need -= total_food_need / group_number

if total_energy > 0:
    print(f"You are ready for the quest. You will be left with {total_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {total_food_need:.2f} food and {total_water_need:.2f} water.")
