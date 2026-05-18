#Working with Loop
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

import random
number = random.randint(1,10)

isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn't it. Try again.".format(guess))
        




# import random

# # print("Welcome to Guess the Number!")
# # print("The rules are simple. I will think of a number, and you will try to guess it.")

# number = random.randint(1, 50)

# isGuessRight = False 

# while isGuessRight != True:
# guess = int(input("Guess a number between 1 and 10: "))

# if guess == number:
# print(f'You guessed {guess}. That is correct!')
# isGuessRight = True
# # another option to use break
# else:
# print(f"You guessed {guess}. Sorry that isn't corrent.")
# if guess < number:
# print("Too low!")
# else:
# print("Too high!")