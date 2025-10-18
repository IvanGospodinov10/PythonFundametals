numbers = list(map(int, input().split()))

average_number = sum(numbers) / len(numbers)
filtered_numbers = [number for number in numbers if number > average_number]
if filtered_numbers == []:
    print("No")
else:
    print(" ".join(str(num) for num in sorted(filtered_numbers, reverse=True)[:5]))
