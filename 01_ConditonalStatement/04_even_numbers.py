add_numbers = int(input())

for add_numbers in range (1, add_numbers + 1):
    number = int(input())

    if  not number % 2 == 0:
        print(f"{number} is odd!")
        break
else:
    print("All numbers are even.")

