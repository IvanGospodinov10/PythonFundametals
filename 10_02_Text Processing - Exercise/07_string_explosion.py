some_string = input()
final_string = ""
strength = 0
for index in range(len(some_string)):
    # Explosion marker
    if some_string[index] == ">":
        final_string += ">"
        strength += int(some_string[index+1])
    # Explosion
    elif strength > 0:
        strength -= 1
    # No Explosion and No Explosion marker
    else:
        final_string += some_string[index]
print(final_string)