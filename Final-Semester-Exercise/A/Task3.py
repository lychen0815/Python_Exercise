#首先要处理task1的保存的file,然后
import re

file = open("32009682_clean_dialogue.txt", "r")

data = file.readline()
#删除最末尾处的符号(这个地方注意一下看有没有更好的处理方式)
pattern = re.sub(r"\)]", "", data)

#分组
dialogue_list = pattern.split("),")


res = []
for r in dialogue_list:
    #抛弃之前的符号
    res.append(r[2:])
print(res)
#根据角色分组
new_dialogue = ""

for i in res:
    dialogue = "".join(i)
    new_dialogue += (dialogue + "\n")


##以下内容是正式处理内容











