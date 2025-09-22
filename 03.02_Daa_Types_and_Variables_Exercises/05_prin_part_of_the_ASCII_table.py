start_number = int(input())
finish_number = int(input())

for character in range(start_number, finish_number + 1):
    if character != finish_number:
        print(f"{chr(character)}",end=' ')
    else:
        print(f"{chr(character)}",end='')