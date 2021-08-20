"""
The average of a list of values is defined as their sum, divided by the number in the set.
For example, the average of the list [3, 5, 8, 2, 2] is (3+5+8+2+2)/5 = 20/5 = 4
Write a program that calculates the average of a list of numbers.
You don’t need to get the list from the user.
"""

list1 = [3, 5, 8, 2, 2]
list_sum = 0
for i in range(0,len(list1)):
    list_sum += list1[i]

list_length = len(list1)
list_average = list_sum / list_length

print("List average is", list_average)

