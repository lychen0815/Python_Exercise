
file = open('32009682_clean_dialogue.txt','r')

data = file.read()

#将文件读出的字符串形式转换为list的形式
dialogue_list = eval(data)

#将文件转换为人能读的懂的格式
new_dialogue = ""

for i in dialogue_list:
    new_tuple = "".join(i)
    new_dialogue += (new_tuple + "\n")
print(new_dialogue)
