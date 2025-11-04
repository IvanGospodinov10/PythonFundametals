words = input().split()

word_occurrences = {}

for word in words:
    key_word = word.lower()
    if key_word not in word_occurrences:
        counter = 1
        word_occurrences[key_word] = counter

    else:
        word_occurrences[key_word] += 1

print(" ".join([word for word, value in word_occurrences.items() if value %2 != 0]))