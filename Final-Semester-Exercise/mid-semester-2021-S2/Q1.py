"""
1. String Statistics(3 Marks)
#CollectiveDatatypes

Implement a function def str_stat(a_string): that accepts a string as an argument and return a dictionary that stores the count of each lower-case character.

Example: str_stat('AaAbbCc') will return {'a': 1, 'b': 2, 'c': 1}

Note: You can assume a_string must be a string
"""
def str_stat(a_string):
    new_dict = {}
    for i in a_string:
        if (i.islower()):
            if i not in new_dict:
                new_dict[i] = 1
            else:
                new_dict[i] += 1
    return new_dict

print(str_stat('AaAbBCc'))