import random
import sys

secretNumber = random.randint(1, 20)
tried = 0
print('I am thinking of a number between 1 and 20.')
print('Take a guess.')


def checkGuess(guess):
    difference = abs(guess-secretNumber)
    if difference != 0:
        if difference < 5:
            return 'little'
        else:
            return 'too'


while True:
    guess = int(input())
    tried += 1
    difference = checkGuess(guess)
    if guess < secretNumber:
        print('Your guess is {} low. Guess again'.format(difference))
        continue
    elif guess > secretNumber:
        print('Your guess is {} high. Guess again'.format(difference))
        continue
    else:
        print('Good job! You guessed my number in ' + str(tried) + ' guesses!')
        playAgain = input('Would you like to play again? (y/n)')
        if playAgain == 'y':
            secretNumber = random.randint(1, 20)
            tried = 0
            print('Take a guess.')
            continue
        elif playAgain == 'n':
            print('Thanks for playing!')
            sys.exit()
    sys.exit()
