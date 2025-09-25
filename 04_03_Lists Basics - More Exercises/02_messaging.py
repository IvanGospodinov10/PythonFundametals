sequence_of_numbers = input().split()
string_message = input()
message = ''
for num in sequence_of_numbers:
    sum_n = 0
    index = 0
    for n in num:
        sum_n += int(n)
    index = sum_n % len(string_message)
    message += string_message[index]
    string_message = string_message[:index] + string_message[index + 1:]

print(message)


