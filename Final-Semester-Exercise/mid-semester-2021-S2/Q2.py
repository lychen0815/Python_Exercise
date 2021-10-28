"""
2. Special Numbers(3 Marks)
#NumericOperations

A defective number is a number  𝑛  for which the sum of divisors is less than  2×𝑛 .

A divisor  𝑚  of number  𝑛  means  𝑛  is completely divisible by  𝑚 , i.e. the remainder of  𝑛𝑚  is 0.

For example,  21  is a defective number because the sum of divisors of  21  is  1+3+7+21=32<21∗2=42
Please implement a function def is_defective(a_num): which accepts a positive integer as argument, then evaluate and return whether the integer is a defective number (True) or not(False).

For example, is_defective(21) will return True.

*you can assume a_num is always valid.
"""
def is_defective(a_num):
    defective_list = []
    for i in range(1,a_num + 1):
        if a_num % i == 0:
            defective_list.append(i)
    sum_factors = sum(defective_list)
    if sum_factors < a_num * 2:
        return True
    else:
        return False

print(is_defective(21))