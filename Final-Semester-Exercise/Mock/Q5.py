"""
Q5 : This question is about Python collective data types.
"""
def lists_to_dictionary(key_list, value_list):
    if len(key_list)==0 and len(value_list)==0:
        return {}
    new_dict = dict(map(lambda x,y:[x,y],key_list,value_list))
    return new_dict
print(lists_to_dictionary(["one", "two", "three"] , [1, 2, 3]))
