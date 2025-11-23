import re

phone_number_list = input()

pattern = "\\+359-2-[0-9]{3}-[0-9]{4}\\b|\\+359 2 [0-9]{3} [0-9]{4}\\b"

valid_phone_numbers = re.findall(pattern, phone_number_list)
print(', '.join(valid_phone_numbers))