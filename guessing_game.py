# Guess the number game
import random

name = input('Hello, what is your name: ')

print('Well, ' + name + ', I am thinking of a number between 1 and 20')
number = random.randint(1, 20)

for guessesTaken in range(1, 7):
    guess = int(input('Take a guess: '))

    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    else:
        break # This condition is for the correct guess!

if guess == number:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(number))
