import re

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
names = input().split(", ")

valid_names = []
for name in names:
    match = re.match(pattern, name)
    if match:
        print(match.group(), end=' ')
