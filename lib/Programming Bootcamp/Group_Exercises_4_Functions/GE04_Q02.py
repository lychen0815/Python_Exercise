"""
2.Write a program that gets the product of a list of numbers. If you’re looking for a challenge, figure out a way to get that list of numbers from the user (hint: look at the Fizz Buzz game).
	Try to use functions!
"""

def numGame(num):
    if num % 3 == 0 and num % 5 != 0:
        print("Fizz")
    elif num % 5 == 0 and num % 3 != 0:
        print("Buzz")
    elif num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
    else:
        print(num)

game_num = int(input('Please enter a number >>>'))

game_result = numGame(game_num)

