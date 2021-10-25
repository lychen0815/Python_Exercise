it = iter(range(0,5))
while True:
    try:
        x = next(it)
        #print(x)
    except:
        break

'''
Demo 1: check string contain unique characters
Given a string variable, e.g.,
a_str = 'sfasfjkhfiosa'
Write the code to check whether a_str contains all unique characters.
'''

a_str = 'sgelihibahfs'
flag = True
chars = []
for i in a_str:
    if i in chars:
        print('a_str has duplicate characters')
        flag = False
        break
    else:
        chars.append(i)

if flag:
    print("a_str has all unique characters")


"""
Demo 2: checking palindrome
Given a variable, e.g.,
a_str = 'abaninaba' Write the code to check whether a_str is a palindrome or not.
"""

a_str = 'deep'
if a_str == a_str[::-1]:
    print("true")
else:
    print("false")






