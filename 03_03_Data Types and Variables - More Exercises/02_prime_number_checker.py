number = int(input())

if number <= 1:
    print("False")
else:
    is_prime = True
    for num in range(2, int(number ** 0.5) + 1):

        if number % num == 0:
            is_prime = False
            break
    print(f"True" if is_prime else "False")