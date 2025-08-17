first_number = int(input())
second_number = int(input())
third_number = int(input())

if first_number > second_number and first_number > third_number:
    print(first_number)
elif second_number > first_number and second_number > third_number:
    print(second_number)
else:
    print(third_number)


# num1, num2, num3 = int(input()), int(input()), int(input())
# print(max(num1, num2, num3))