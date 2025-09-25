numbers_str = list(map(int, input().split(", ")))
zero = []
non_zero = []

for num in numbers_str:

    if num == 0:
        zero.append(num)
    else:
        non_zero.append(num)
print(non_zero + zero)