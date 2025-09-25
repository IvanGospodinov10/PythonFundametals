sequence_of_numbers = input().split()

absolut_value = []

for num in sequence_of_numbers:
    absolut_value.append(abs(float(num)))

print(absolut_value)