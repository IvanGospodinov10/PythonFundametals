number = int(input())

synonyms_words = {}

for num in range(number):
    word = input()
    synonym = input()

    if word not in synonyms_words:
        synonyms_words[word] = [synonym]
    else:
        synonyms_words[word].append(synonym)

for key,value in synonyms_words.items():
    print(f"{key} - {', '.join(value)}")
