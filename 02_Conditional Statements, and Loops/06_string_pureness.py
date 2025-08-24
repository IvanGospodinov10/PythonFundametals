number_of_string = int(input())

is_true = True

for current_words in range(number_of_string):
    word = input()
    for index, char in enumerate(word):
        if char == ',' or char == '.' or char == '_':
            is_true = False
            print(f"{word}, is not pure!")
            break

    if is_true:
        print(f"{word}, is pure.")

