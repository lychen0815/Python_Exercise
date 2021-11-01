def selection_sort(a_list):
    sorted_list = a_list[:] # make a copy of the original list
    for iter in range(len(sorted_list) - 1):
        smallest_idx = iter
        # search for index of smallest value behind
        for index in range(iter + 1, len(sorted_list)):
            # if current item is smaller than current smallest item, update index of smallest item
            if sorted_list[index] < sorted_list[smallest_idx]:
                smallest_idx = index
        sorted_list[iter], sorted_list[smallest_idx] = sorted_list[smallest_idx], sorted_list[iter] # swap target index with the smallest index behind
    return sorted_list
selection_sort([5,3,4,1,2])