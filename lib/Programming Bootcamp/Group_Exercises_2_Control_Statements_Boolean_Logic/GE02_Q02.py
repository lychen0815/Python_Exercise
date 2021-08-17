"""
At university, we have a grading system where the mark you receive determines the grade you get. The system is as follows:
N	0 - 49
P	50 - 59
C	60 - 69
D	70 - 79
HD	80 - 100
Write a program that gets a numeric mark from the user and returns the respective grade.
"""

user_mark = int(input("please enter your numeric mark >>>"))

if user_mark >= 80:
    print("Your grade is HD")
elif user_mark >= 70:
    print("Your grade is D")
elif user_mark >= 60:
    print("Your grade is C")
elif user_mark >= 50:
    print("Your grade is P")
else:
    print("Your grade is N")