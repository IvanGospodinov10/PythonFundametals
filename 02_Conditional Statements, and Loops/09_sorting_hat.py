name = input()
is_voldemort = False

while name != 'Welcome!':
    name_length = len(name)

    if name == 'Voldemort':
        print(f"You must not speak of that name!")
        is_voldemort = True
        break

    if name_length < 5:
        house = f"{name} goes to Gryffindor."
    elif name_length == 5:
        house = f"{name} goes to Slytherin."
    elif name_length == 6:
        house = f"{name} goes to Ravenclaw."
    else:
        house = f"{name} goes to Hufflepuff."

    print(house)

    name = input()

if not is_voldemort:
    print(f"Welcome to Hogwarts.")
