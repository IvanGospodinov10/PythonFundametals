initial_energy = int(input())
energy = initial_energy
battle_won = 0
while True:
    distance = input()
    if distance == "End of battle":
        break
    energy -= int(distance)
    if energy <= 0:
        if energy == 0:
            battle_won += 1
        break
    battle_won += 1
    if battle_won % 3 == 0:
        energy += battle_won
if energy <= 0:
    print(f"Not enough energy! Game ends with {battle_won} won battles and {energy} energy")
else:
    print(f"Won battles: {battle_won}. Energy left: {energy}")