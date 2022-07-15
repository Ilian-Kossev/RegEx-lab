
store = {}

command = input()
sold_food_quantity = 0
while not command == 'Complete':
    command, quantity, food = command.split(' ')
    quantity = int(quantity)
    if command == 'Receive':
        if quantity <= 0:
            command = input()
            continue
        if food in store:
            store[food] += quantity
        store[food] = quantity

    elif command == 'Sell':
        if food not in store:
            print(f'You do not have any {food}.')
            command = input()
            continue

        elif store[food] < quantity:
            print(f"There aren't enough {food}. You sold the last {store[food]} of them.")
            sold_food_quantity += store[food]
            del store[food]
            command = input()
            continue

        store[food] -= quantity
        sold_food_quantity += quantity
        print(f'You sold {quantity} {food}.')
        if store[food] == 0:
            del store[food]

    command = input()

for item, quant in store.items():
    print(f'{item}: {quant}')
print(f'All sold: {sold_food_quantity} goods')