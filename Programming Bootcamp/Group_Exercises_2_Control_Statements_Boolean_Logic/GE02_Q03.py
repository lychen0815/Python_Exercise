"""
Create a calculator. Ask the user for 2 numbers and an operator.  Perform the operation and display the result to the console.
"""

#input first number
user_num = int(input("please enter a number >>>"))

#input operator
user_operate = input("please enter the operator(+,-,*,/) >>>")

#input second number
user_num2 = int(input("please enter another number >>>"))

if user_operate == "+":
    user_result = user_num + user_num2
elif user_operate == "-":
    user_result = user_num - user_num2
elif user_operate == "*":
    user_result = user_num * user_num2
elif user_operate == "/":
    user_result = user_num / user_num2
else:
    print("Invalid Operator")

print("Your answer is " + str(user_result))
