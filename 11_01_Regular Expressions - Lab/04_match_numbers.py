import re

pattern = r'(^|(?<=\s))-?[1-9]\d*(\.\d+)?($|(?=\s))'

text = input()
numbers = [m.group() for m in re.finditer(pattern, text)]

print(" ".join(numbers))
