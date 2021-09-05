"""
Write a function def checkArmstrong(filename) that reads the file with filename and prints out whether numbers in each line of the file are Armstrong numbers or not.

Note: An Armstrong number is an integer such that the sum of cubes of its digits is equal to the number itself. For example, 371 is an Armstrong number since 3^3 + 7^3 + 1^3 = 371.
"""

def checkArmstrong(num):
    num1 = num // 100
    a = num % 100
    num2 = a // 10
    num3 = a % 10
    if num1 ** 3 + num2 ** 3 + num3 ** 3 == num:
        print(True)
    else:
        print(False)



checkArmstrong(118)