"""
1. String Manipulation
Write a funtion def convertString(str_list, N): that takes in a list of strings(str_list)
and an integer (N) and convert the string into uppercase if the length of string is greater than N.
The function will return the converted list.
"""
#正确的解法
def covertString1(str_list,N):

    for i in range(len(str_list)):
        if len(str_list[i]) > N:
            #使用索引来对其赋值
            str_list[i] = str_list[i].upper()
        print("covertString1 is ", str_list)
        return str_list
covertString1(["Programming", "Coding", "Python", "Hello"],7)


#以下是错误示范
def covertString2(str_list,N):
    for i in str_list:
        if len(i) > N:
            #不可以这样直接去赋值
            i = i.upper()
        print("covetString2 is ",str_list)
        return str_list
covertString2(["Programming", "Coding", "Python", "Hello"],7)