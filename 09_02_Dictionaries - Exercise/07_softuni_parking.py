number_of_commands = int(input())
parking_register_data = {}

for num in range(number_of_commands):
    command_text = input().split()
    command = command_text[0]
    username = command_text[1]

    if command == "register":
        license_plate_number = command_text[2]
        if username not in parking_register_data.keys():
            parking_register_data[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")
    if command == "unregister":
        if username in parking_register_data.keys():
            del parking_register_data[username]
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

for username, license_plate_number in parking_register_data.items():
    print(f"{username} => {license_plate_number}")
