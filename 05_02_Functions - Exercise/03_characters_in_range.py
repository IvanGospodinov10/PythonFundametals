def character_in_range(char_one: str, char_two: str):
    """

    :param char_one:
    :param char_two:
    :return:
    """
    char_list = ''
    for num in range(ord(char_one) + 1, ord(char_two)):
        char_list += chr(num) + " "
    return char_list

# my_list = character_in_range(character_one, character_two)
# print(my_list)
character_one = input()
character_two = input()
print(character_in_range(character_one, character_two))