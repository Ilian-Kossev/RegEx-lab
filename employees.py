import re


regex = r'^(?P<names>[A-Z][a-z]{2,}\s[A-Z][a-z]{2,})#+(?P<position>[A-Z][a-z]+(&[A-Z][A-Za-z]+)?(&[A-Z][A-Za-z]+)?)[0-9]{2}(?P<company>[A-Z][A-Za-z0-9]+\s(Ltd\.|JSC))$'
number = int(input())
for _ in range(number):
    line = input()
    match = re.search(regex, line)
    if match:
        string = f"{match.group('names')} is {match.group('position')} at {match.group('company')}"
        final_string = string.replace('&', ' ')
        print(final_string)

