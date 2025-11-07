text_number = input()
phone_book = {}

while True:
    if "-" not in text_number:
        break
    name, phone_number = text_number.split("-")
    if name not in phone_book.keys():
        phone_book[name] = phone_number
    else:
        phone_book[name] = phone_number

    text_number = input()
# print(phone_book)
numbers_check = int(text_number)
for num in range(numbers_check):
    name_check = input()
    if name_check in phone_book.keys():
        print(f"{name_check} -> {phone_book[name_check]}")
    else:
        print(f"Contact {name_check} does not exist.")
