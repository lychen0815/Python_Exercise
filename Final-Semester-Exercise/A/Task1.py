
import re

def extractDialogue():

    file = open("input_script.txt",'r')
    data = file.read()

    #删除所有含(),[]的句子
    pattern = re.sub(r"\(.*?\)|\[.*?\]", "", data)

    # 删除)之后的空格(也就是有两个空格的位置）(删除完（）之后，其后有空格，这步就是在处理这个）但不匹配换行符),但保留一个空格
    delete_space = re.sub(r'[^\S\r\n]{2,}', " ", pattern)

    #删除开头几个带：by的句子
    pattern2 = re.sub(r".*by:.*", "", delete_space)

    #删除所有空行
    pattern3 = "".join([s for s in pattern2.splitlines(True) if s.strip()])

    #按照换行的的形式，将他们分开
    list_pattern = pattern3.split('\n')

    #删除所有不带:的句子
    for line in list_pattern:
        if re.search(r"^((?!:).)*$", line) != None:
            list_pattern.remove(line)


    #将list分开成，第一个项是角色名称，第二个是他们的台词
    #同时将list转换成tuple,将tuple内部的每一项也进行转换

    new_list = []
    for i in range(len(list_pattern)):
        new_line = list_pattern[i].split(":")
        new_list.append(tuple(new_line))

    return new_list




#将提取好的文字放到新文件中

dialogue = extractDialogue()
'''
print(dialogue)
new_dialogue = ""

for i in dialogue:
    new_tuple = "".join(i)
    new_dialogue += (new_tuple + "\n")
#print(new_dialogue)
'''
with open('32009682_clean_dialogue.txt', 'w') as f:
    f.write(str(dialogue))
