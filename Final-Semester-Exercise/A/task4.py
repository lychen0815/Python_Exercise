import re

file = open('32009682_clean_dialogue.txt','r')

data = file.read()

dialogue_list = eval(data)

new_dialogue = ""

for i in dialogue_list:
    new_tuple = "".join(i)
    new_dialogue += (new_tuple + "\n")
print(new_dialogue)

