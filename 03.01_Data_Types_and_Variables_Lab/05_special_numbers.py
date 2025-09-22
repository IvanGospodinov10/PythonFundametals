number = int(input())
# special_number = 0

for num_range in range(1, number +1):
    special_number = 0

    for num in str(num_range):
        special_number += int(num)


    if special_number == 5 or special_number == 7 or special_number == 11:
        print(f"{num_range} -> True")
    else:
        print(f"{num_range} -> False")