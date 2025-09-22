my_string = input()

my_list = my_string.split(", ")
# print(my_list[-1])
counter = len(my_list) -1
if my_list[-1] == 'wolf':
    print(f'Please go away and stop eating my sheep')


else:
    for element in my_list:
        if element == 'wolf':
            print(f'Oi! Sheep number {counter}! You are about to be eaten by a wolf!')
        counter -= 1