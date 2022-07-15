import re

text = input()
reg = r'(?P<Day>\d{2})(?P<separator>[/\.-])(?P<Month>[A-Z][a-z]{2})(?P=separator)(?P<Year>\d{4})'
result = re.finditer(reg, text)
for item in result:
    current_date = item.groupdict()

    print(f"Date: {current_date['Day']}, Month: {current_date['Month']}, Year: {current_date['Year']}")