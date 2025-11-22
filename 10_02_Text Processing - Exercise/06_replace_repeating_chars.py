some_string = input()

final_string = ""

for character in some_string:
    if not final_string or character != final_string[-1]:
        final_string += character
print(final_string)