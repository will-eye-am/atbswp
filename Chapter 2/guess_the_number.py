# This is a guess the number game
import random

secret_number = random.randint(1,20)
print('I am thinking of a number bewteen 1 and 10.')

# Ask player to guess up to  6 times
for guesses_taken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        break # correct guess

if guess == secret_number:
    print('Great! You guessed the number in ' + str(guesses_taken) + ' tries!')
else:
    print('Fail! The number was ' + str(secret_number) + '!')