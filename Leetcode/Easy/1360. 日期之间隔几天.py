"""
请你编写一个程序来计算两个日期之间隔了多少天。

日期以字符串形式给出，格式为 YYYY-MM-DD，如示例所示。

示例 1：

输入：date1 = "2019-06-29", date2 = "2019-06-30"
输出：1
示例 2：

输入：date1 = "2020-01-15", date2 = "2019-12-31"
输出：15

"""
#引入datetime库
from datetime import datetime
date1 = input("Please enter first date: ")
date2 = input("Please enter second date: ")

result = abs((datetime.strptime(date1,'%Y-%m-%d') - datetime.strptime(date2,'%Y-%m-%d')).days)
print(result)