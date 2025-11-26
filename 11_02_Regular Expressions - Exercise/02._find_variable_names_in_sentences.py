import re

some_text = input()
pattern = r"\b_([A-Za-z0-9]+)\b"
matches = re.findall(pattern, some_text)
print(",".join(matches))
