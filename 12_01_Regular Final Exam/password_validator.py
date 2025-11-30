def upper_case(password, index):
    pass_list = []
    for i in range(len(password)):
        if i == int(index):
            letter = password[i].upper()
            pass_list.append(letter)
        else:
            pass_list.append(password[i])
    new_password = "".join(pass_list)
    print(new_password)
    return new_password


def lower_case(password, index):
    pass_list = []
    for i in range(len(password)):
        if i == int(index):
            letter = password[i].lower()
            pass_list.append(letter)
        else:
            pass_list.append(password[i])

    new_password = "".join(pass_list)
    print(new_password)
    return new_password


def insert_letter(password, index, letter):
    pass_list = []
    for character in password:
        pass_list.append(character)
    pass_list.insert(int(index), letter)

    new_password = "".join(pass_list)
    print(new_password)
    return new_password


def replace(password, character, value):
    pass_list = []
    current_char = ord(character)
    new_sum_value = current_char + int(value)
    new_char = chr(new_sum_value)
    for char_x in password:
        if char_x == character:
            pass_list.append(new_char)
        else:
            pass_list.append(char_x)
    new_password = "".join(pass_list)
    print(new_password)
    return new_password


def password_validation(password):
    if len(password) < 8:
        print("Password must be at least 8 characters long!")
    if not all(char.isalnum() or char == "_" for char in password):
        print("Password must consist only of letters, digits and _!")
    if not any(char.isupper() for char in password):
        print("Password must consist at least one uppercase letter!")
    if not any(char.islower() for char in password):
        print("Password must consist at least one lowercase letter!")
    if not any(char.isdigit() for char in password):
        print("Password must consist at least one digit!")


receive_the_password = input()

while True:
    command = input()
    if command == "Complete":
        break

    command = command.split(" ")
    action = command[0]
    if action == "Make":
        if command[1] == "Upper":
            receive_the_password = upper_case(receive_the_password, command[2])
        elif command[1] == "Lower":
            receive_the_password = lower_case(receive_the_password, command[2])
    elif action == "Insert":
        receive_the_password = insert_letter(receive_the_password, command[1], command[2])
    elif action == "Replace":
        receive_the_password = replace(receive_the_password, command[1], command[2])
    elif action == "Validation":
        password_validation(receive_the_password)
