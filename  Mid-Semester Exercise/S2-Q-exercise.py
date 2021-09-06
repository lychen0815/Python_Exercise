def sumOfUniqe(nums):
    total_dict = {}
    total_sum = 0
    for num in nums:
        if num in total_dict.keys():
            total_dict[num] += 1
        else:
            total_dict[num] = 1
    for key,value in total_dict.items():
        if value == 1:
            total_sum += key
    return total_sum

print(sumOfUniqe([1,1,1,1,1]))