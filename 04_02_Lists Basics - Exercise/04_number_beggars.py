food_list = list(map(int, input().split(", ")))
beggars = int(input())

beggars_list = list(range(1,beggars + 1))
output_beggars_bags = []


for beggar_num in beggars_list:
    counter = beggar_num - 1
    beggar_outcome = 0
    for food_bags in food_list:

        if len(food_list) > counter:
            beggar_outcome += food_list[counter]
            counter += beggars
        else:
            break

    output_beggars_bags.append(beggar_outcome)

print(output_beggars_bags)