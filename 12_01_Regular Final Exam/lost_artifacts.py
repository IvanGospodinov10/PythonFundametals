import re

encrypted_message = input()

pattern = r"[*^]([A-Za-z\s]{6,})[*^][^A-Za-z0-9]*\++(-?\d+\.?\d+,-?\d+\.?\d+)\++"

matches = re.findall(pattern, encrypted_message)
# print(matches)

if matches:
    for artifact, coordinates in matches:
        print(f"Found {artifact} at coordinates {coordinates}.")
else:
    print("No valid artifacts found.")