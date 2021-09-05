"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
来源：力扣（LeetCode）
"""

def longestCommonPrefix(strs):
    res = ""
    for tmp in zip(*strs):
        #print(tmp)
        tmp_set = set(tmp)
        #print(tmp_set)
        if len(tmp_set) == 1:
            res += tmp[0]
        else:
            break
    #print(res)


longestCommonPrefix(["flower","flow","flight"])

