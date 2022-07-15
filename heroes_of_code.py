n = int(input())
heroes = {}
while not n == 0:
    n -= 1
    hero, hit_points, mana_points = input().split(' ')
    heroes[hero] = {
        'hp': int(hit_points),
        'mp': int(mana_points),
    }

command = input()
while not command == 'End':
    if command.startswith('CastSpell'):
        _, hero, mana_points_needed, spell_name = command.split(' - ')
        if heroes[hero]['mp'] >= int(mana_points_needed):
            heroes[hero]['mp'] -= int(mana_points_needed)
            print(f"{hero} has successfully cast {spell_name} and now has {heroes[hero]['mp']} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif command.startswith('TakeDamage'):
        _, hero, damage, attacker = command.split(' - ')
        heroes[hero]['hp'] -= int(damage)
        if  heroes[hero]['hp'] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]['hp']} HP left!")
        else:
            del heroes[hero]
            print(f"{hero} has been killed by {attacker}!")

    elif command.startswith('Recharge'):
        _, hero, points = command.split(' - ')
        mana_points = int(points)
        heroes[hero]['mp'] += int(mana_points)
        if heroes[hero]['mp'] >= 200:
            mana_points -= (heroes[hero]['mp'] - 200)
            heroes[hero]['mp'] = 200
        print(f"{hero} recharged for {mana_points} MP!")

    elif command.startswith('Heal'):
        _, hero, points = command.split(' - ')
        hit_points = int(points)
        heroes[hero]['hp'] += int(hit_points)
        if heroes[hero]['hp'] >= 100:
            hit_points -= (heroes[hero]['hp'] - 100)
            heroes[hero]['hp'] = 100
        print(f"{hero} healed for {hit_points} HP!")

    command = input()


for hero, _ in heroes.items():
    if heroes[hero]['hp'] > 0:
        print(hero)
        print(f"  HP: {heroes[hero]['hp']}")
        print(f"  MP: {heroes[hero]['mp']}")

