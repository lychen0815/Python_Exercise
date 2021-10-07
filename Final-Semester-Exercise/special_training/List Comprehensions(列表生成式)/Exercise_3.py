"""
练习一：编写名为collatz（number）的函数；实现的功能：参数为偶数时，打印number// 2;参数为奇数时，打印3*number + 1
"""
num = int(input("Please enter a num >>> "))

print(num //2) if num % 2 == 0 else print(num * 3 +1)

"""
练习二：使用for循环，对列表元素的类型进行更改
"""

s = "51 5000 10000"
k,a,b = [int(i) for i in s.split(" ")]
print(k,a,b)


