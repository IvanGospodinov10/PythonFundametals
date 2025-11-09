banned_words = input().split(", ")
text = input()

for word in banned_words:
    replaced_word = len(word) * "*"
    while word in text:
        text = text.replace(word, replaced_word)
print(text)

