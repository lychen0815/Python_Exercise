#这个文件主要是针对Task2B做处理，把硬编码全部去除。首先写入文件的格式转换成人类能懂的格式，接着将正则里面匹配的文字写成变量形式

import re

file = open('32009682_clean_dialogue.txt','r')

data = file.read()

#将文件读出的字符串形式转换为list的形式
dialogue_list = eval(data)

#将文件转换为人能读的懂的格式
new_dialogue = ""

for i in dialogue_list:
    new_tuple = "".join(i)
    new_dialogue += (new_tuple + "\n")

#进行角色匹配
name = "Ross"
character_pattern = re.findall(r'^' + name + '.*',new_dialogue,re.MULTILINE)
#character_pattern = re.findall(r"^Ross.*",new_dialogue,re.MULTILINE)

character_dialogue = ''
for line in character_pattern:
    new_pattern = "".join(line)
    character_dialogue += (new_pattern + "\n")

#character = re.sub(r"Ross", "", character_dialogue)

character = re.sub(r'' + name, "", character_dialogue)

print(character)
