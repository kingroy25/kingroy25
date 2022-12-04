# Shell Game

# Create a list.
# Create a user input to guess where the ball (0) is.
# Create fuction to check if the user and the position of the ball in a list matches.

from random import shuffle

def list_shuffle(mylist):
    shuffle(mylist)
    return mylist

mylist = ['O','','']

def user_guess():
    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input("Choose 0, 1 or 2!")

    return int(guess)

def check_user(mylist,guess):
        if mylist[guess] == 'O':
            print('You win!!!')
        else:
            print("Try Again")
            print(mylist)

# Shuffle the list.
mixed_up = list_shuffle(mylist)

# User input.
guess = user_guess()
print(guess)

# Check if it's correct.
print(check_user(mixed_up,guess))