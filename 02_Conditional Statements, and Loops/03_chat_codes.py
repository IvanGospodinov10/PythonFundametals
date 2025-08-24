number_of_message = int(input())

for message in range(number_of_message):
    message_num = int(input())
    current_message = ''

    if message_num == 88:
        current_message = "Hello"
    elif message_num == 86:
        current_message = "How are you?"
    elif (message_num != 86 or message_num != 88) and message_num < 88:
        current_message = 'GREAT!'
    else:
        current_message = 'Bye.'

    print(current_message)
