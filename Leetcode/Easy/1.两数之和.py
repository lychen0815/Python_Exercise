"""
1. 两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

来源：力扣（LeetCode）
"""

#method 1:


def sum(nums, target):
    if len(nums) < 2:
        return
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]


print(sum([2,7,11,15],9))

'''
#method 2

def sum(nums, target):
    dict1 = {}
    for i in range(len(nums)):
        num = target - nums[i]
        if num not in dict1:
            dict1[nums[i]] = i
        else:
            return [dict1[num], i]
nums = [2,7,11,15]
print(sum(nums,9))
'''













