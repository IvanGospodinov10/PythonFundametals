number_of_snowballs = int(input())

max_weight = 0
max_time = 0
max_quality = 0
max_value = 0

for snowball in range (1, number_of_snowballs + 1):

    weight_of_the_snowball = int(input())
    time_needed = int(input())
    quality = int(input())

    current_value = (weight_of_the_snowball // time_needed) ** quality

    if current_value > max_value:
        max_value = current_value
        max_weight = weight_of_the_snowball
        max_time = time_needed
        max_quality = quality

print(f"{max_weight} : {max_time} = {max_value} ({max_quality})")

