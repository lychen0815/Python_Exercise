
file = open('32009682_clean_dialogue.txt','r')

data = file.read()

#将文件读出的字符串形式转换为list的形式
dialogue_list = eval(data)


#将一个角色下的对话汇总在一起
separate_dialogue = {}

for line in dialogue_list:
    if line[0] in separate_dialogue.keys():
        separate_dialogue[line[0]] += (line[1] + '\n')
    else:
        separate_dialogue[line[0]] = (line[1] + '\n')



#将对应角色的话写到其文件中
for i in separate_dialogue:
    with open('32009682_'+ i.lower() +'.txt', 'w') as f:
        f.write(str(separate_dialogue[i]))


####################################

file = open("32009682_ross.txt",'r')

data = file.read()

#去掉所有的换行符
new_data = data.replace("\n","")

character_dialogue = new_data.split(' ')

#找出一个角色里面不重复的单词
unique_word = set(character_dialogue)

############################
from collections import Counter
import re
#根据要求，不区分大小写，所以统一换成小写
lower_data = data.lower()

new_list = data.split("\n")

separate_word = []
for i in new_list:

    list_dialogue = i.split(" ")
    print(list_dialogue)
    c = Counter(list_dialogue)  # 取出每个单词出现的个数

















