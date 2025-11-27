import re


sentence = input()
searched_text = input()

# pattern = r"(?i)\{searched_text}\b"
pattern = fr"\b{searched_text}\b"
matches = re.findall(pattern, sentence, re.IGNORECASE)

print(len(matches))
