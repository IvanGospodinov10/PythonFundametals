number_of_strings = int(input())
word = input()

my_list = []
for string in range(number_of_strings):
    add_string = input()
    my_list.append(add_string)
print(my_list)

for index in range(len(my_list) -1, -1, -1):
    element = my_list[index]
    if word not in element:
        my_list.remove(element)
print(my_list)