"""
1. String Manipulation
Write a funtion def convertString(str_list, N): that takes in a list of strings(str_list)
and an integer (N) and convert the string into uppercase if the length of string is greater than N.
The function will return the converted list.
"""

def convertString(str_list, N):
    for i in range(len(str_list)):
        if len(str_list[i]) > N:
            str_list[i] = str_list[i].upper()
    print(str_list)
    return str_list

convertString(["Programming", "Coding", "Python", "Hello"], 7)