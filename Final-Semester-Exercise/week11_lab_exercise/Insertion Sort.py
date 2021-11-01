def insertion_sort(a_list):
    sorted_list = a_list[:] # make a copy of the original list
    for iter in range(1, len(sorted_list)):
        target_idx = iter
        # swap with previous item until the previous item is smaller
        # or until we reach start of list
        while target_idx > 0:
            if sorted_list[target_idx] < sorted_list[target_idx - 1]:
                sorted_list[target_idx], sorted_list[target_idx - 1] = sorted_list[target_idx - 1], sorted_list[target_idx]
                target_idx -= 1
            else:
                break
    return sorted_list
insertion_sort([5,1,7,2])