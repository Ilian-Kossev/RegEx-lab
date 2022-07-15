import re


regex = r'(?<=^)@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+(?=$)'
num = int(input())
default_barcode_group = '00'


while not num == 0:
    num -= 1
    barcode = input()

    default_barcode_group_active = True

    match_obj = re.search(regex, barcode)
    if match_obj:
        result = match_obj.group()
        barcode_group = ''
        for x in result:
            if x.isnumeric():
                barcode_group += x
                default_barcode_group_active = False

        if default_barcode_group_active:
            print(f'Product group: {default_barcode_group}')
        else:
            print(f'Product group: {barcode_group}')
    else:
        print('Invalid barcode')




