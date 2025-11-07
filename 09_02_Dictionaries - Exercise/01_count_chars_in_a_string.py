input_string = input().split()
my_string = ""

for items in input_string:
    my_string += items

character_dict = {}

for character in my_string:

    if character not in character_dict.keys():
        counter = 1
        character_dict[character] = counter
    else:
        character_dict[character] += 1

for key, value in character_dict.items():
    print(f"{key} -> {value}")