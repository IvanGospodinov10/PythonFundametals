number_of_message = int(input())

if number_of_message == 88:
    print("Hello")
elif number_of_message == 86:
    print("How are you?")
elif (number_of_message != 86 or number_of_message != 88) and number_of_message < 88:
    print('GREAT!')
else:
    print('Bye')