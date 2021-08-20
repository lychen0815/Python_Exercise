"""
Modify your calculator to handle invalid inputs.
For the purposes of these exercises we will consider two types of errors caused by invalid inputs:
-A divide by zero error
-Entering the wrong data type as input for a number
a.Find what inputs result in the aforementioned errors.
b.Handle the case where the input results in a divide by zero error
c.Extension: Handle the case where the input is the wrong type (Hint: have a look at what isnumeric() does)
"""



#input first number
user_num = input("please enter a number >>>")
#check whether the input is number or not
if user_num.isnumeric():
    user_num = int(user_num)
else:
    print("This isn't a number, please enter a number!")

#input operator
user_operate = input("please enter the operator(+,-,*,/) >>>")

#input second number
user_num2 = input("please enter another number >>>")
if user_num2.isnumeric():
    user_num2 = int(user_num2)
else:
    print("This isn't a number, please enter a number!")

if user_operate == "+":
    user_result = user_num + user_num2
elif user_operate == "-":
    user_result = user_num - user_num2
elif user_operate == "*":
    user_result = user_num * user_num2
elif user_operate == "/":
    #Check whether zero is the divisor or not
    if(user_num2 == 0):
        print("zero can't do divisor")
    else:
        user_result = user_num / user_num2
else:
    print("Invalid Operator")

if(user_num2 == 0):
    print("please enter another number")
else:
    print("Your answer is " + str(user_result))


