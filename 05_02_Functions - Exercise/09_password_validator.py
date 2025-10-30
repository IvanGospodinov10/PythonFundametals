def is_valid_password(password):
    is_valid = True

    # Проверка за дължина
    if not (6 <= len(password) <= 10):
        print("Password must be between 6 and 10 characters")
        is_valid = False

    # Проверка за символи – само букви и цифри
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False

    # Проверка за поне 2 цифри
    digit_count = sum(1 for char in password if char.isdigit())
    if digit_count < 2:
        print("Password must have at least 2 digits")
        is_valid = False

    # Ако всички проверки са успешни
    if is_valid:
        print("Password is valid")


# 📥 Примерен вход от потребителя
password = input("Enter password to validate: ")
is_valid_password(password)