character_list = input().split(", ")

# ascii_dict = {}


ascii_dict = {char: ord(char) for char in character_list}
print(ascii_dict)

# for char in character_list:
#     key = char
#     value = ord(char)
#     ascii_dict[key] = value
# print(ascii_dict)