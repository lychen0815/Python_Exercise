"""
Q5 : This question is about Python collective data types.
"""
def lists_to_dictionary(key_list, value_list):
    new_dict = {}
    for i in range(len(key_list)):
        new_dict.update({key_list[i]: value_list[i]})
    return new_dict
print(lists_to_dictionary(["one", "two", "three"] , [1, 2, 3]))