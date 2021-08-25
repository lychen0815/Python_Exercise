"""
4.Create a game where the user must correctly guess a positive integer number between 1 and 100.
The user should be notified whether their guess was “lower” or “higher” than the target number.
	Remember:
-Use functions to group code
-Try to have functions that only do one “thing” (e.g. print a message, validate user input, check what message to display)
-Check for invalid inputs, notifying the user and re-prompting for a valid input

Hint: Start by listing out each thing that your program needs to do.
This is usually a good start point for figuring out what functions you need to implement!

"""
import random

random_num = random.randint(1,100)

def is_valid(guess):
    if not guess.isnumeric():
        return False
    return 1 <= int(guess) <= 100

def guess_number():
    guess = input("Enter guess >> ")

    while not is_valid(guess):
        print("please enter a number between 1 and 100")
    return int(guess)

user_num = -1

while random_num != user_num:
    user_num = guess_number()
    if user_num < random_num:
        print("Lower! Try again")
    elif user_num > random_num:
        print("Higher! Try again")


print("Congratulation!")