some_text = input()

for index in range(len(some_text)):
    if some_text[index] == ":":
        if index + 1 < len(some_text):
            print(some_text[index: index + 2])