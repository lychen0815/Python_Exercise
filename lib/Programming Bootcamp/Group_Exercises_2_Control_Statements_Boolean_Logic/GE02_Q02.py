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

#Add judgment condition
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
    
    
    
    """
    method2
# Initialise variable
grade = ''

# Get input
mark = int(input("Enter mark: "))

# Mark to grade
if 0 <= mark < 50:  # Same as mark >= 0 and mark < 50
    grade = 'N'
elif 50 <= mark < 60:  # mark >= 50 and mark < 60
    grade = 'P'
elif 60 <= mark < 70:  # mark >= 60 and mark < 70
    grade = 'C'
elif 70 <= mark < 80:  # mark >= 70 and mark < 80
    grade = 'D'
elif 80 <= mark:  # Can replace with else
    grade = 'HD'

# Display result
print(mark, " (", grade, ")")

"""
