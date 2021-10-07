"""
https://www.cnblogs.com/uthnb/p/9594418.html

练习一： 假设有20个学生，成绩在60-100之间，筛选出成绩在90分以上的学生

解析： 随机生成60-100之间的学生和成绩；然后在生成的字典中选择输出
"""
import random

stuInfo = {'student' + str(i):random.randint(60,100) for i in range(20)}

print({name:score for  name,score in stuInfo.items()  if score > 90})
"""
练习二： 将字典中的key值和value值调换

解析：
"""
d = {'a':1,'b':2,'c':3}

print({v:k for k,v  in  d.items()})

print({k:k.upper() for k,v in d.items()})
"""
练习三：大小写合并，Key值最终全部为小写

解析：
"""
d = {'a':1,'b':2,'c':3,'A':5}

print({k.lower():d.get(k.upper(),0)+d.get(k.lower(),0) for k,v in d.items()})