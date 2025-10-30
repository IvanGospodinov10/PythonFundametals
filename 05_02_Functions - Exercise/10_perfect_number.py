def is_perfect_number(number):
    divisors_sum = sum(i for i in range(1, number) if number % i == 0)

    if divisors_sum == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

num = int(input())
is_perfect_number(num)