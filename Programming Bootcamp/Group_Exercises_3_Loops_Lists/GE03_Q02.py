"""
Print the following sequence of numbers using a loop
29, 24, 19, 14, 9, 4, -1
"""

#method1
#for i in range(29,-2,-5):
 #   print(i)


# method2
max_value = 29
min_value = -1

i = max_value
while i >= min_value:
    print(i)
    i -= 5
