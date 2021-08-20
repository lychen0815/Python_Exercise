"""
Create a program that takes in an integer and prints out
a.“Fizz” if it is divisible by 3
b.“Buzz” if it is divisible by 5
c.“FizzBuzz” if it is divisible by both 3 and 5
d.Itself if none of the above holds
	eg.
	input “1” -> output “1”
	input “2” -> output “2”
	input “3” -> output “Fizz”
	input “5” -> output “Buzz”
	input “15” -> output “FizzBuzz”
	Be careful of the ordering of your conditional statements!
"""

input_number = int(input("please enter a integer>>> "))

if input_number % 3 == 0 and input_number % 5 != 0:
    print('Fizz')
elif input_number % 5 == 0 and input_number % 3 != 0:
    print('Buzz')
elif input_number % 3 == 0 and input_number % 5 == 0:
    print("FizzBuzz")
else:
    print(input_number)
