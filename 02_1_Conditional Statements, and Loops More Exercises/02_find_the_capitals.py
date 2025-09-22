word = input()

list_word = []
new_list = []

for text in word:
    list_word.append(text)

for index, char in enumerate(list_word):
    if char.isupper():
        new_list.append(index)

print(new_list)



# word = "SofUnI"
# for char in word:
#     if char.isupper():
#         print(f"{char}", end='')