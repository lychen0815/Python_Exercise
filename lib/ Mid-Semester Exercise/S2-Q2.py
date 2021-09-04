"""
2. DataTypes
You are given an list of integers. T
he unique elements of a list are the elements that appear exactly once in the array.
Write a function def sumOfUnique(nums): that takes nums as a list of integers
and return the sum of all the unique elements of nums.

"""
def sumOfUnique(nums):

    value_count = {}

    for i in nums:
        if i in value_count.keys():

          value_count[i] += 1
        else:
          value_count[i] = 1
    print(value_count)

    sum = 0

    for key,value in value_count.items():
        if value == 1:
            sum += key

    return sum
sumOfUnique([1,2,3,2] )

'''
    nums.sort(reverse=False)
    #new_list = []
    for i in range(len(nums)):
        while i < len(nums):
            if nums[i] == nums[i+1]:
                nums.remove(nums[i+1])
    print(nums)
    return nums


sumOfUnique([1,2,3,2])
'''

'''
n = len(nums)
    new_list = []
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                break
            else:
                new_list.append(nums[i])
                # nums.remove(nums[j])
            # print(nums[i], nums[j])

    print(new_list)
    return new_list
    
'''