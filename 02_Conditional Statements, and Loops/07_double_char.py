while True:
    text = input()

    if text == 'End':
        break
    if text == 'SoftUni':
        continue
    for char in text:
        print((char * 2), end="")
    print()

    # Да се преправи кода да не е с безкраен цикъл а да е с проверка или с for loop