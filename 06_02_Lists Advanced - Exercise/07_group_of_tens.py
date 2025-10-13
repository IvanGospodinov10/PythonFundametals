numbers = list(map(int, input().split(", ")))
group = 10

while numbers:
    list_of_current_group = [number for number in numbers if number <= group]
    print(f"Group of {group}'s: {list_of_current_group}")
    numbers = [number for number in numbers if number not in list_of_current_group]
    group += 10