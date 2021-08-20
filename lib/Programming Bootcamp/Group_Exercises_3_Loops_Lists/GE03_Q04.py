"""
For a given list of integers, determine how many are multiples of 3, e.g. the_list = [2,6,7,10,12,16,18], output should be ‘3’
"""

the_list = [2,6,7,10,12,16,18]
multiple_count = 0

'''
#method1
for i in the_list:
    if i % 3 == 0:
        multiple_count += 1

print(multiple_count)
'''

'''
#method2
for i in range(len(the_list)):
    if i % 3 == 0:
        multiple_count += 1

print(multiple_count)
'''
#method3
i = 0
while i < len(the_list):
    if the_list[i] % 3 == 0:
        multiple_count += 1
    i += 1
print(multiple_count)















