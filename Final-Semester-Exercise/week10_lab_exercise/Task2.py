def bubble_sort(a_list):
    sorted_list = a_list[:] # make a copy of the original list
    for iter in range(1,len(sorted_list)):
        for index in range(len(sorted_list) - iter):
            if sorted_list[index] > sorted_list[index + 1]:
                sorted_list[index], sorted_list[index + 1] = sorted_list[index + 1], sorted_list[index]
    return sorted_list
bubble_sort([3,2,6,7,1,8])