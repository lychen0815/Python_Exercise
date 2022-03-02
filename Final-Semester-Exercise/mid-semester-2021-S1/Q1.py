"""
1. String Manipulation
Write a funtion def convertString(str_list, N): that takes in a list of strings(str_list) and an integer (N) and convert the string into uppercase if the length of string is greater than N. The function will return the converted list.
Example 1

Input: String_list = [“Programming”, “Coding”, “Python”, “Hello”], N = 7

Output: [“PROGRAMMING”, “Coding”, “Python”, “Hello”]

Explanation: Length of “Programming” is 12, which is greater than 7. Other string have less than 7 string length.
"""

def covertString(str_list, N):
    for i in range(len(str_list)):
        if len(str_list[i]) > N:
            str_list[i] = str_list[i].upper()
    return str_list

print(covertString(["Programming", "Coding", "Python", "Hello"], 7))