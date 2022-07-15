import re
text = input()
pattern = r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b'
x = re.findall(pattern, text)
#print(' '.join(x))
print(*x)