"""
给定一个已按照 非递减顺序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。

函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。

来源：力扣（LeetCode）

"""
def sum(numbers, target):
    for i in range(0,len(numbers)-1):
        for j in range(i+1,len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]
print(sum(numbers = [-1,0], target = -1))

#虽目前可以运行，但此题需要改进