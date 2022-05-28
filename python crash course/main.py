"""
simple_message = 'Hello'
print(simple_message)

simple_message = 'Hello world'
print(simple_message)

name = " Kris roller "

print("Hello "+name+", would you like to learn python today?")
print(name.upper())
print(name.lower())
print(name.title())

famous_person = "albert einstein"

print(famous_person.title() + ' once said "A person who never made a mistake
                            'never '
                            'tried anything new."')

print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
"""

# prints the number 8 with different additions
'''
print(4+4)
print(5+3)
print(6+2)
print(7+1)
'''

# Prints my favorite number turing it into a string using the str method

'''
fav_number = 10
print("My favorite number is "+str(fav_number))
'''

# random number guesser
'''
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry guess again. Number too high.')
    print(f'Yay, you guess the number {random_number} correctly! ')

y = int(input('How high would you like to guess?'))
guess(y)
'''

# countdown timer
'''
def count_down(start_number):
    for i in range(-1 ,start_number):
        print(start_number)
        start_number -=1

x = int(input('What number would you like the countdown to start at?'))
count_down(x)
'''

#Password Generator
'''
import random

def make_password(number_of_passwords ,length_of_password):
    password =''
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQUSTUVWXYZ!@#$%^&*' \
                  '()<>?1234567890'
    for _ in range(number_of_passwords):
       print(password.join(random.choice(chars)for _ in range(length_of_password
                                                              )))


x = int(input('How many passwords do you want to generate?'))
y = int(input('What length do you want the passwords to be?'))
make_password(int(x) ,int(y))
'''

