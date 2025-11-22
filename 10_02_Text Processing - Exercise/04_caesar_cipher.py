original_string = input()

encrypted_string = ""

for character in original_string:
    encrypted_letter = chr(ord(character) + 3)
    encrypted_string += encrypted_letter
print(encrypted_string)