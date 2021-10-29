"""
Q6 : This question is about Recursion.
"""
def mystery_func(a_str):
    result = False
    if len(a_str) <= 1:
        result = True
    elif a_str[0] == a_str[len(a_str)-1]:
        result = mystery_func(a_str[1:len(a_str)-1])
    return result
print(mystery_func('deed'))