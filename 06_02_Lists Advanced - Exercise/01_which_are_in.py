first_sequence = input().split(", ")
second_sequence = input().split(", ")
new_list = []

for first_string in first_sequence:
    for second_string in second_sequence:
        if first_string in second_string:
            new_list.append(first_string)
            break
print(new_list)
