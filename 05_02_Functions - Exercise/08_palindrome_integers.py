list_of_positive_integers = input().split(", ")

def palindrome_number(list_of_numbers):
    my_list_of_palindrome = []
    for num in list_of_numbers:
        if num == num[::-1]:
            num = 'True'
        else:
            num = 'False'
        my_list_of_palindrome.append(num)
    return my_list_of_palindrome

for num_ in palindrome_number(list_of_positive_integers):
    print(num_)