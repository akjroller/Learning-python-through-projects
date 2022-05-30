import random

dice_to_roll = input('What type of dice would you like to roll? D4, D6, D8, D10, D12, or D20?')

if dice_to_roll == 'D4' or dice_to_roll == 'd4':
    x = 4
elif dice_to_roll == 'D6' or dice_to_roll == 'd6':
    x = 6
elif dice_to_roll == 'D8' or dice_to_roll == 'd8':
    x = 8
elif dice_to_roll == 'D10' or dice_to_roll == 'd10':
    x = 10
elif dice_to_roll == 'D12' or dice_to_roll == 'd12':
    x = 12
elif dice_to_roll == 'D20' or dice_to_roll == 'd20':
    x = 20
else:
    print('invalid responce')
    quit()

how_many_rolls = input('How many times would you like to roll?')

for i in range(int(how_many_rolls)):
    l=[]
    l.append(random.randint(0,x))
    print(*l)


