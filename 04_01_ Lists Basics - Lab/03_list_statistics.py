numbers = int(input())

positive = []
negative = []

for num in range(numbers):
    add_number = int(input())
    if add_number >= 0:
        positive.append(add_number)
    else:
        negative.append(add_number)

print(f"{positive}\n{negative}")
print(f'Count of positives: {len(positive)}\nSum of negatives: {sum(negative)}')