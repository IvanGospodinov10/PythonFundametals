while True:
    current_string = input()
    if current_string == "end":
        break

    print(f"{current_string} = ", end='')
    print(current_string[::-1])