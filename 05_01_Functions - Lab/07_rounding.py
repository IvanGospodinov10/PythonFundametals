numbers = input().split()

def rounding_numbers(text):
    round_list = []
    for num in text:
        round_list.append(round(float(num)))
    return round_list

print(rounding_numbers(numbers))