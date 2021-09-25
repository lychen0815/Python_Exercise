
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

