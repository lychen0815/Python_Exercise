"""
Q2 : This question is about Control Structures and Testing.
"""
def create_dict(input_list):
    new_str = ''
    new_dict = {}
    for word in input_list:
        for char in word:
            if char.isalpha():
                new_str += char.lower()
    for letter in new_str:
        if letter not in new_dict:
            new_dict[letter] = 1
        else:
            new_dict[letter] += 1
    return new_dict


def find_tuples(input_dic,threshold_value):
    new_list = []
    if len(input_dic) == 0:
        return []
    for k,v in input_dic.items():
        if type(v) == int or type(v) == float:
            if v > threshold_value:
                input_list = []
                input_list.append(k)
                input_list.append(v)
                new_tuple = tuple(input_list)
                new_list.append(new_tuple)
    return new_list


def main():

    create_dict(["HELLO world", "python is best"])
    print(find_tuples({"z": "xyz", "f": 2, "9": 8, "6": 11}, 7))

if __name__ =="__main__":
    main()