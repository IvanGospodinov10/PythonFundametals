list_of_integer = list(map(int, input().split(" ")))
count_of_numbers_to_remove = int(input())

for repeat in range(count_of_numbers_to_remove):
    num_to_remove = min(list_of_integer)
    list_of_integer.remove(num_to_remove)

print(", ".join(str(num) for num in list_of_integer))


# list_of_integer.sort(reverse=True)

# list_of_integer= list_of_integer[:(len(list_of_integer) - count_of_numbers_to_remove)]