gifts = list(input().split(" "))
# print(names_of_the_gifts)

command = ""

while True:
    command = input()
    if command == "No Money":
        break

    parts = command.split()
    action = parts[0]
    if action == "OutOfStock":
        gift_to_remove = parts[1]
        gifts = ["None" if gift == gift_to_remove else gift for gift in gifts]
    elif action == "Required":
        gift_to_add = parts[1]
        index = int(parts[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift_to_add
    elif action == "JustInCase":
        gift_to_add = parts[1]
        gifts[-1] = gift_to_add

final_gifts = [gift for gift in gifts if gift != "None"]
print(" ".join(final_gifts))

