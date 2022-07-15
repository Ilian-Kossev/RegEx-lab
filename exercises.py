import re

# data = input()
# regex = r'\d+'
# total = []
# while not data == '':
#     res = re.findall(regex, data)
#     total.extend(res)
#     data = input()
# print(*total)


# data = input()
# regex = r'((?<=^_)|(?<=\s_))[A-Za-z0-9]+\b'
# res = [x.group() for x in re.finditer(regex, data)]
# print(','.join(res))


# data = input()
# word = input()
# regex = f'\\b{word}\\b'   - escaping \ in string
# regex = fr'(?i)\b{word}\b'  - ignorecase directly in pattern
# regex = fr'\b{word}\b'  - using raw string
# res = [x.group() for x in re.finditer(regex, data, re.IGNORECASE)]
# print(len(res))

# data = input()
# regex = r'(^|(?<=\s))[A-Za-z0-9]+[\._-]?[A-Za-z0-9]+@[A-Za-z]+-?[A-Za-z]+(\.[A-Za-z]+-?[A-Za-z]+)+($|(?=\s))'
# match = re.finditer(regex, data)
# for x in match:
#     print(x.group())



# (?<=^)>>(?P<item>\w+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)(?=$)

# regex = r'(?<=^)>>(?P<item>[A-Za-z]+)<<(?P<price>[0-9]+(\.[0-9]+)?)\!(?P<quantity>[0-9]+)(?=$)'
# list_items = []
# total_money_spent = 0
# data = input()
# while not data == 'Purchase':
#     match_object = re.search(regex, data)
#     if not match_object:
#         data = input()
#         continue
#
#     input_info = match_object.groupdict()
#     furniture_item = input_info['item']
#     furniture_price = float(input_info['price'])
#     quantity = int(input_info['quantity'])
#     total_money_spent += furniture_price * quantity
#     list_items.append(furniture_item)
#     data = input()
#
# print('Bought furniture:')
# for item in list_items:
#     print(item)
# print(f'Total money spend: {total_money_spent:.2f}')


string = input()
regex = r'(^|(?<=\s))w{3}\.[A-Za-z0-9-]+(\.[a-z]+)+($|(?=[\s,\.:;\!\?/]))'
while string:
    match_object = re.search(regex, string)
    if not match_object:
        string = input()
        continue
    print(match_object.group())
    string = input()