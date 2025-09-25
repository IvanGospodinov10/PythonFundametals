def sum_numbers(a: int, b: int):
    return a + b


def subtract(sum_, c: int):
    return sum_ - c


number_one = int(input())
number_two = int(input())
number_three = int(input())

sum_of_two_num = sum_numbers(number_one, number_two)
subtract_num = subtract(sum_of_two_num, number_three)
print(subtract_num)
