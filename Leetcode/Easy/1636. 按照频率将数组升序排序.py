"""
给你一个整数数组 nums ，请你将数组按照每个值的频率 升序 排序。如果有多个值的频率相同，请你按照数值本身将它们 降序 排序。

请你返回排序后的数组。
"""

def frequencySort(test_list):
    new_dic = {}
    new_list = []
    #和2021S1期中的第二题一样，dict的key值记录值，value记录其出现的个数
    for i in test_list:
        if i in new_dic.keys():
            new_dic[i] += 1
        else:
            new_dic[i] = 1

    items_list = list(new_dic.items())
    #-x[0]代表逆序,x[1]代表按照第二项也就是value-出现次数的值进行排序
    items_list.sort(key=lambda x:(x[1],-x[0]))

    for item in items_list:
        new_item = list(item)
        if new_item[1] == 1:
            new_list.append(new_item[0])
        while new_item[1] != 1:
            new_list.append(new_item[0])
            new_item[1] -= 1
            if new_item[1] == 1:
                new_list.append(new_item[0])
                break
    return new_list

frequencySort([-1,1,-6,4,5,-6,1,4,1])