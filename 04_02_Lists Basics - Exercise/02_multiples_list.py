factor = int(input())
counter = int(input())
index = 0

my_list = list(range(1,counter + 1))

for num in my_list:
    number = num * factor
    my_list[index] = number
    index += 1
print(my_list)
