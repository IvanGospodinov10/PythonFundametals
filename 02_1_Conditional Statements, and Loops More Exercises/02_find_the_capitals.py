word = input()

list_word = []

for text in word:
    list_word.append(text)

for index, char in enumerate(list_word):
    if char.isupper():
        print(f"{index}", end='')


# word = "SofUnI"
# for char in word:
#     if char.isupper():
#         print(f"{char}", end='')