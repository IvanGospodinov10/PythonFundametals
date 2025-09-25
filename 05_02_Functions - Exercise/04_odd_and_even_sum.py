single_number = int(input())

def even_or_odd_sum(number: int):
    even_sum_digits = 0
    odd_sum_digits = 0
    for num in str(number):
        if int(num) % 2 == 0:
            even_sum_digits += int(num)
        else:
            odd_sum_digits += int(num)
    return f"Odd sum = {odd_sum_digits}, Even sum = {even_sum_digits}"
print(even_or_odd_sum(single_number))