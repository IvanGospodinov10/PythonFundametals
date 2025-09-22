string_input = input()

my_list = string_input.split(" ")
invert_list = []

for num in my_list:
    invert_num = -int(num)
    invert_list.append(invert_num)

print(invert_list)