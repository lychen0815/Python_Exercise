"""
Write code to calculate the factorial of a number given by the user. (Note: The factorial of a number is the product of all numbers smaller than it. Eg. 5! = 5*4*3*2*1)
"""


input_number = int(input("please enter a number >>>"))

result = 1

for i in range(input_number,1,-1):
    result *= i

print("The result is " + str(result))