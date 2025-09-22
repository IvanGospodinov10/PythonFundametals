my_string = input().lower()

keyword = ['Sand', 'Water', 'Fish', 'Sun']

counter = 0
for word in keyword:
    characters = 0
    while characters <= len(my_string) - len(word):
        if my_string[characters:characters + len(word)] == word.lower():
            counter += 1
            characters += len(word)
        else:
            characters += 1
print(counter)
