positive_number = int(input())
boundary_number = int(input())
number_to_delete = boundary_number


while (number_to_delete % positive_number) != 0:
    number_to_delete -= 1

print(number_to_delete)