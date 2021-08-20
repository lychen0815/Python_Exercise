"""
For a given list of integers, determine how many are multiples of 3, e.g. the_list = [2,6,7,10,12,16,18], output should be ‘3’
"""

input_list = [2, 6, 7, 10, 12, 16, 18]

count_num = 0

'''
#method1
for i in input_list:
    if i % 3 == 0:
        count_num += 1

print("There are", count_num, "multiples of 3")

'''
'''
#method2
for i in range(len(input_list)):
    item = input_list[i]
    if item % 3 == 0:
        count_num += 1
print("There are", count_num, "multiples of 3")
'''

#method3

i = 0
while i < len(input_list):
    item = input_list[i]
    if item % 3 == 0:
        count_num += 1
    i += 1
print("There are", count_num, "multiples of 3")
