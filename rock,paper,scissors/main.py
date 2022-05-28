import random

rps = ['R', 'P', 'S']
print('welcome to rock, paper, scissors')
rounds = input('How many rounds would you like to play?')
x = 0
score = 0

while x != int(rounds):
    user_input = input('do you choose [R]ock [P]aper or [S]cissors?')
    comp_input = random.choice(rps)
    if user_input == comp_input:
        print("You got a tie")
        x+=1
        score = score
        print(f'Your score is: {score}')
    elif user_input == 'R' and comp_input == 'S':
        print("You chose Rock and the computer chose scissors")
        print('You Win')
        x += 1
        score+=1
        print(f'Your score is: {score}')
    elif user_input == 'R' and comp_input == 'P':
        print("You chose Rock and the computer chose paper")
        print('You loose')
        x += 1
        score -= 1
        print(f'Your score is: {score}')
    elif user_input == 'P' and comp_input == 'R':
        print("You chose paper and the computer chose rock")
        print('You win')
        x += 1
        score += 1
        print(f'Your score is: {score}')
    elif user_input == 'P' and comp_input == 'S':
        print("You chose paper and the computer chose scissors")
        print('You loose')
        x += 1
        score -= 1
        print(f'Your score is: {score}')
    elif user_input == 'S' and comp_input == 'R':
        print("You chose scissors and the computer chose rock")
        print('You loose')
        x += 1
        score -= 1
        print(f'Your score is: {score}')
    elif user_input == 'S' and comp_input == 'P':
        print("You chose scissors and the computer chose paper")
        print('You win')
        x += 1
        score += 1
        print(f'Your score is: {score}')
    else:
        print('Invalid input')
        print(f'Your score is: {score}')
