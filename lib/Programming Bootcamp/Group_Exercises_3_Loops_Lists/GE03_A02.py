"""
Create a program which takes as input a list of numbers from the user. You may find it useful to Google how Python’s “split()” method works on strings. Ask your tutor if you need help.

Then, for each of the numbers in the list:
●if it is divisible by 3, print “Fizz”
●if it is divisible by 5, print “Buzz”
●if it is divisible by both 3 and 5, print “FizzBuzz”
●otherwise just print the number itself

Figure out a way to print the output on one line separated by a comma
e.g. for the list [1, 2, 3, 4, 5, 6, 7, 8, 9] the output would be:
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz

"""
number_list = []
result = []
input_list = input("Enter list of csv numbers (e.g. 1,2,3): ").split(',')

for string in input_list:
    number_list.append(int(string))

for element in number_list:
    if element % 3 == 0 and element % 5 == 0:
        result.append("FizzBuzz")
    elif element % 3 == 0:
        result.append("Fizz")
    elif element % 5 == 0:
        result.append("Buzz")
    else:
        result.append(str(element))
print(",".join(result))