'''
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

来源：力扣（LeetCode）

'''

#这个解法不是删除重复的数，它原数是不删除的（比如：【1，2，2】，输出【1，2】，而不是【1】

def removeDulicates(nums):
    nums.sort()
    n = len(nums)
    a = 0
    for i in range(1,n):
        if nums[i-a] == nums[i-a-1]:
            nums.pop(i-a)
            a += 1
    return len(nums),nums

#print(removeDulicates([0,0,1,1,1,2,2,3,3,4]))

print(removeDulicates([1,1,2]))
