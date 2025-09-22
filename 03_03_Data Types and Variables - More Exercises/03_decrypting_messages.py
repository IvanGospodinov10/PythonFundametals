key = int(input())
lines = int(input())

message = ''

for character in range(lines):
    char = input()
    decrypting_char = chr(ord(char) + key)
    message += decrypting_char

print(message)