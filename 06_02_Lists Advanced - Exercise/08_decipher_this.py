secret_message = input().split()
decipher_message = []

for word in secret_message:
    word = list(word)
    number_as_string = ""

    for index in range(len(word)):
        if word[index].isdigit():
            number_as_string += word[index]
        else:
            break
    number_as_letter = chr(int(number_as_string))
    word = [number_as_letter] + word[index:]
    word[1], word[-1] = word[-1], word[1]
    decipher_message.append("".join(word))
print(" ".join(decipher_message))