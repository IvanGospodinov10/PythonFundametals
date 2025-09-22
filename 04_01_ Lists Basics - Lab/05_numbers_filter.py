number_to_add = int(input())

list_of_numbers = []

for num in range(number_to_add):
    number_input = int(input())
    list_of_numbers.append(number_input)

action = input()

filtered_numbers = []
if action == "even":
    for numbers in list_of_numbers:
        if numbers % 2 == 0:
            filtered_numbers.append(numbers)
elif action == "odd":
    for numbers in list_of_numbers:
        if numbers % 2 != 0:
            filtered_numbers.append(numbers)
elif action == "negative":
    for numbers in list_of_numbers:
        if numbers < 0:
            filtered_numbers.append(numbers)
elif action == "positive":
    for numbers in list_of_numbers:
        if numbers >= 0:
            filtered_numbers.append(numbers)
print(filtered_numbers)