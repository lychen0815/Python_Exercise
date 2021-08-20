"""
user_input = input("Please enter numbers separated by comma >>> ")

user_int = user_input.split(",")
print((user_int))

if user_input.isdigit():
    print('hi')
else:
    print('wrong')

"""


"""
import itertools
import re
user_input = input("Please enter numbers separated by comma >>> ")
user_int  = re.findall(r'\d+', user_input)
print(type(user_input))
print(user_input)
#user_int = user_input.split(",")
#print(type(user_int))
#这个地方加上一个判断字符串里面是不是数字的

user_int2 = list(map(int, user_int))

user_permutation = list(itertools.permutations(user_int2, 2))

print(user_permutation)
"""

import itertools
import re
user_input = input("Please enter numbers separated by comma >>> ")
user_int  = re.findall(r'\d+', user_input)
user_int2 = list(map(int, user_int))
user_permutation = list(itertools.permutations(user_int2, 2))
print(user_permutation)


'''
b = "100"
if b.isdigit():a
    print("right")
else:
    print("try again")

import re
a = "100,a,12"
#a = re.sub("\D","",a)
a = re.findall(r'\d+', a)
#a = list(map(int, re.findall('-?\d+', a)))
print(a)

'''


"""
testList = "1, 2, 'a', [1, 2]"

for i in testList:
    if type(i.isdigit()):
        print("yes")
    else:
        testList.remove(i)
print(testList)
"""


