'''
Prompt the user to enter a new password until the user enters a valid password.
A valid password has the following properties:
a.More than 6 characters
b.End in an integer
c.Extension: Contain at least one lowercase letter and one uppercase.
There are many ways to implement this, ask your tutor if you don’t know where to start!
'''

user_passed = input("please enter a new password >>>")

if len(user_passed) <= 6:
    print("You must enter more than 6 characters!")


for item in user_passed:
    if item.islower():
        print('You must enter at least one uppercase letter!')
        break
for j in user_passed:
    if j.isupper():
        print('You must enter at least one lowercase letter!')
        break

if not user_passed[-1].isdigit():
    print('You must enter end in an integer')