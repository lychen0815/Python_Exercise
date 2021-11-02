def binary_search(item_dic, target_item):
    sorted_list = list(sorted(item_dic.items(),key=lambda x: x[0]))
    clear_list = [x[1] for x in sorted_list]
    return clear_list


print(binary_search({3:"a", 13:"c", 5: "b", -5: "d"}, "b"))