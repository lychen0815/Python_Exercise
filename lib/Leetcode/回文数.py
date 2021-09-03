'''
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。

来源：力扣（LeetCode）
'''

def isPalindrome(num):
    num1 = str(num)

    reverse_num1 = num1[::-1]

    if reverse_num1 == num1:
        print("true")
    else:
        print("false")

isPalindrome(10)