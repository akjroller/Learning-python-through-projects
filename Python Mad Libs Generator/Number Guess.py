import random

number_to_guess = 0


print(f"Hello, thanks for playing my number guessing game! Good luck have fun!")
x = input("How high would you like the range of numbers to be?")
try:
    number_to_guess = random.randint(1, int(x))
    score = int(x)*10
    reduce = int(x)*5/10
except:
    print("Sorry expected a number your provided a string")
    quit()

print(f"Ok I am thinking of a number between 1 and {x}")
while True:
    print(f"your current score is {score}")
    user_answer = input("What number am I thinking of?")
    if int(user_answer) < number_to_guess:
        print("Try again, your number was too low")
        score = int(score) - int(reduce)
    elif int(user_answer) > number_to_guess:
        print("Try again, your number was too high")
        score = int(score) - int(reduce)
    else:
        print(f"Good job you got the correct answer of {number_to_guess}"
              f" your final score is {score}")
        break
