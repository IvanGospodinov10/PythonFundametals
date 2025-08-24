while True:
    text = input()

    if text == 'End':
        break
    if text == 'SoftUni':
        continue
    for char in text:
        print((char * 2), end="")
    print()