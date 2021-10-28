"""
2. DataTypes
You are given an list of integers. The unique elements of a list are the elements that appear exactly once in the array. Write a function def sumOfUnique(nums): that takes nums as a list of integers and return the sum of all the unique elements of nums.
"""

def sumOfUnique(nums):
    unique_dict = {}
    sum_unique = 0
    for i in nums:
        if i not in unique_dict:
            unique_dict[i] = 1
        else:
            unique_dict[i] += 1
    for j in unique_dict:
        if unique_dict[j] == 1:
            sum_unique += j
        else:
            sum_unique = 0
    return sum_unique

print(sumOfUnique([1,2,3,4,5]))