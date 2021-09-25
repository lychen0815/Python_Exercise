#这个文件进行了硬编码，所有的人名匹配和文件写入全部写死（不是个好方法，所以后面的文件对此进行了更改，2A是正式可以使用的文件，之后的版本都是不断改进的）

import re

def separateDialogus(character):
    file = open("32009682_clean_dialogue.txt","r")

    data = file.read()
    #判断传进来的角色名称
    if character == "Ross":
        character_pattern = re.findall(r"^Ross.*",data,re.MULTILINE)
    elif character == "Chandler":
        character_pattern = re.findall(r"^Chandler.*", data, re.MULTILINE)
    elif character == "Joey":
        character_pattern = re.findall(r"^Joey.*", data, re.MULTILINE)
    elif character == "Phoebe":
        character_pattern = re.findall(r"^Phoebe.*", data, re.MULTILINE)
    elif character == "Gunther":
        character_pattern = re.findall(r"^Gunther.*", data, re.MULTILINE)
    elif character == "Monica":
        character_pattern = re.findall(r"^Monica.*", data, re.MULTILINE)
    elif character == "Receptionist":
        character_pattern = re.findall(r"^Receptionist.*", data, re.MULTILINE)
    elif character == "Janice Voice":
        character_pattern = re.findall(r"^Janice Voice.*", data, re.MULTILINE)
    elif character == "Phoebe and Rachel":
        character_pattern = re.findall(r"^Phoebe and Rachel.*", data, re.MULTILINE)
    elif character == "The Instructor":
        character_pattern = re.findall(r"^The Instructor.*", data, re.MULTILINE)

    character_dialogue = ''
    for line in character_pattern:
        new_pattern = "".join(line)
        character_dialogue += (new_pattern + "\n")

    #删除角色名称，只留下他对应的话语
    if character == "Ross":
        character = re.sub(r"Ross", "", character_dialogue)
    elif character == "Chandler":
        character = re.sub(r"Chandler", "", character_dialogue)
    elif character == "Joey":
        character = re.sub(r"Joey", "", character_dialogue)
    elif character == "Phoebe":
        character = re.sub(r"Phoebe", "", character_dialogue)
    elif character == "Gunther":
        character = re.sub(r"Gunther", "", character_dialogue)
    elif character == "Monica":
        character = re.sub(r"Monica", "", character_dialogue)
    elif character == "Receptionist":
        character = re.sub(r"Receptionist", "", character_dialogue)
    elif character == "Janice Voice":
        character = re.sub(r"Janice Voice", "", character_dialogue)
    elif character == "Phoebe and Rachel":
        character = re.sub(r"Phoebe and Rachel", "", character_dialogue)
    elif character == "The Instructor":
        character = re.sub(r"The Instructor", "", character_dialogue)
    return character


ross = separateDialogus("Ross")
chandler = separateDialogus("Chandler")
joey = separateDialogus("Joey")
phoebe = separateDialogus("Phoebe")
gunther = separateDialogus("Gunther")
monica = separateDialogus("Monica")
receptionist = separateDialogus("Receptionist")
janice_voice = separateDialogus("Janice Voice")
phoebe_rachel = separateDialogus("Phoebe and Rachel")
instructor = separateDialogus("The Instructor")

#将对应角色名的台词分别写进对应的角色中

with open('32009682_ross.txt', 'w') as f:
    f.write(ross)

with open('32009682_chandler.txt', 'w') as f:
    f.write(chandler)

with open('32009682_joey.txt', 'w') as f:
    f.write(joey)

with open('32009682_phoebe.txt', 'w') as f:
    f.write(phoebe)

with open('32009682_gunther.txt', 'w') as f:
    f.write(gunther)

with open('32009682_monica.txt', 'w') as f:
    f.write(monica)

with open('32009682_receptionist.txt', 'w') as f:
    f.write(receptionist)

with open('32009682_janice_voice.txt', 'w') as f:
    f.write(janice_voice)

with open('32009682_phoebe_rachel.txt', 'w') as f:
    f.write(phoebe_rachel )

with open('32009682_instructor.txt', 'w') as f:
    f.write(instructor)









