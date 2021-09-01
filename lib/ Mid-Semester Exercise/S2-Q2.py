"""
2. DataTypes
You are given an list of integers. T
he unique elements of a list are the elements that appear exactly once in the array.
Write a function def sumOfUnique(nums): that takes nums as a list of integers
and return the sum of all the unique elements of nums.

"""


def sumOfUnique(nums):
    """
    A function that sums up all the non-duplicate items in the given list of integers
    Args:
        1. nums(list): A list of integers
    Returns:
        1. int: The sum of non-duplicate items in nums
    """
    value_count = {}  # initialise a dictionary that stores the count of each number in the given list, key is the number, value is the count of that number

    for num in nums:  # iterate through the given list of integers
        if num in value_count.keys():  # if the current number already exists in the key of the value_count dictionary
            value_count[num] += 1  # add the count of that number(value of that key) by 1
        else:  # if the current number does not exit in the key of the dictionary
            value_count[num] = 1  # create a new key for the number, and assign the count of that number as 1

    sum = 0  # initialise a variable that records the sum of non-duplicate values

    for key, value in value_count.items():  # iterate through all items in the dictionary, dict().items() returns a list of tuples, where each tuple is a key-value pair
        if value == 1:  # if the count of the number is 1 (i.e. non-duplicate)
            sum += key  # add the number to the sum
    print(sum)
    return sum
sumOfUnique([1,2,3,2] )