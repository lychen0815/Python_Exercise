"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

来源：力扣（LeetCode）
"""
def reverseNum(num):


#part A: method one of this question : Turn the integer into a string, and then reverse the string

    num1 = str(num)
    #method 1 of reverse String : use slice
    reverse_num1 = int(num1[len(num1)::-1])

    print(reverse_num1)

    #method 2 of reverse String: use loop
    '''
    num2 = []
    index = len(num1)
    while index > 0:
        num2 += num1[index - 1]
        index = index -1
    print(num2)
    '''
    # method 3 of reverse String : use join && reversed
    '''
    reverse_string = ''.join(reversed(num1))
    print(reverse_string)

    print(reversed(num1))
    '''

'''
#part B: method two of this question
    res = 0
    while (num != 0):
        tmp = int(num % 10)
        #Determine whether it is greater than the maximum 32-bit integer
        if (res > 214748364 or (res == 214748364 and tmp > 7)):
            return 0
        #Determine whether it is less than the minimum 32-bit integer
        if (res < -214748364 or (res == -214748364 and tmp < -8)):
            return 0
        res = res * 10 + tmp
        num /= 10
    print(res)
'''

reverseNum(123)
