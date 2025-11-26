import re
text = input()

matches_numbers = []
pattern = r"\d+"

while text:
    matches = re.findall(pattern, text)
    if matches:
        matches_numbers += matches
    text = input()

print(" ".join(matches_numbers))