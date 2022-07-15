import re
pattern = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'
data = input()
matches = re.finditer(pattern, data)
for item in matches:
    print(item.group(), end=' ')
# matches = [item.group() for item in matches]
# print(*matches)