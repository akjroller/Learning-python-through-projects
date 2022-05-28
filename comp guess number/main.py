import random

print("Hello, I will try to guess your number!")
x = input("Your number is between 0 and what?")

start_num = random.randint(0, int(x))

while True:

    print(f"I think your number is {start_num}")
    high_lower = input(f"is the number higher or lower than {start_num}? H for higher or L for lower C for correct")
    if high_lower == 'H':
        higher = random.randint(int(start_num) + 1, int(x))
        start_num = higher
        print('ok, your number was higher')
    elif high_lower == 'L':
        lower = random.randint(0, int(start_num - 1))
        start_num = lower
        print('ok, your number was lower')
    elif high_lower == 'C':
        print(f'Yay I got it right your number is {start_num}')
        break
    else:
        print('Sorry that was invalid input')
        continue
