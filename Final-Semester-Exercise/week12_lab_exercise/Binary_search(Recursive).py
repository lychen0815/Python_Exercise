def rec_binary_search(the_list, target_item):
# repeatedly divide the list into two halves
# as long as the target item is not found
# the list cannot be further divided i.e. item is not found
    if len(the_list) == 0:
        return False
    else:
        # find the mid position
        mid = len(the_list) // 2
        # check if target item is equal to middle item
        if the_list[mid] == target_item:
            return True
        # check if target item is less than middle item
        # search lower half
        elif target_item < the_list[mid]:
            smaller_list = the_list[:mid]
            return rec_binary_search(smaller_list, target_item)
        # check if target item is greater than middle item
        # search upper half
        else:
            larger_list = the_list[mid+1:]
            return rec_binary_search(larger_list, target_item)

print(rec_binary_search([20,51,54,59,75,76,78,89,92],92))