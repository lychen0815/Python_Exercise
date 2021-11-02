def bubble_sort(item_dic):
    item_list = [[k,v] for k,v in item_dic.items()]
    for iter in range(1,len(item_list)):
        for idx in range(0,len(item_list)-iter):
            if item_list[idx][0] > item_list[idx+1][0]:
                item_list[idx],item_list[idx + 1] = item_list[idx+1],item_list[idx]
    sorted_list = [x[1] for x in item_list]
    print(sorted_list)
    return sorted_list

def binary_search(item_dic, target_item):
    binary_list = bubble_sort(item_dic)
    left_idx = 0
    right_idx = len(binary_list)-1
    while left_idx <= right_idx:
        middle_idx = (left_idx + right_idx) // 2
        if binary_list[middle_idx] == target_item:
            return middle_idx
        elif binary_list[middle_idx] > target_item:
            right_idx = middle_idx - 1
        else:
            left_idx = middle_idx + 1
    return False


print(binary_search({3: "a", 13: "c", 5: "b", -5: "d"}, "d"))
