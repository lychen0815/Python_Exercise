"""
Q5 : This question is about Python collective data types.
"""
def lists_to_dictionary(key_list, value_list):
    new_dict = dict(map(lambda x, y: [x, y], key_list, value_list))
    print(new_dict)
lists_to_dictionary(["one", "two", "three"] , [1, 2, 3])