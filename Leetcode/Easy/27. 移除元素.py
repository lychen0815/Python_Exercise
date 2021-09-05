'''
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

来源：力扣（LeetCode）
'''

def removeElement(nums,val):
    '''
    #这种解法是有问题的，因为删除的时候指针位置变了，所以如果去测试下面的这个数组，会漏掉第二个2这里
    for i in nums:
        if i == val:
            nums.remove(i)
    return nums,len(nums)
    '''

    #要使用双指针的思想
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] == nums[j]
            i += 1
    return i




print(removeElement([0,1,2,2,3,0,4,2],2))