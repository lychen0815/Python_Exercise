"""
Write a function def checkArmstrong(filename) that reads the file with filename and prints out whether numbers in each line of the file are Armstrong numbers or not.

Note: An Armstrong number is an integer such that the sum of cubes of its digits is equal to the number itself. For example, 371 is an Armstrong number since 3^3 + 7^3 + 1^3 = 371.
"""

def checkArmstrong(filename):
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            sum_char = 0
            for char in line:
                new_char = int(char) ** 3
                sum_char += new_char
            if sum_char == int(line):
                print("True")
            else:
                print("False")
checkArmstrong('input.txt')