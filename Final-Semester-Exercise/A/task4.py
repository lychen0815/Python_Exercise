# Task2的所有代码全部含进了task3


file = open('32009682_clean_dialogue.txt', 'r')

data = file.read()

# 将文件读出的字符串形式转换为list的形式
dialogue_list = eval(data)

# 将一个角色下的对话汇总在一起
separate_dialogue = {}

for line in dialogue_list:
    if line[0] in separate_dialogue.keys():
        separate_dialogue[line[0]] += (line[1] + '\n')
    else:
        separate_dialogue[line[0]] = (line[1] + '\n')

# 将对应角色的话写到其文件中
for i in separate_dialogue:
    with open('32009682_' + i.lower() + '.txt', 'w') as f:
        f.write(str(separate_dialogue[i]))

# 以下是Task3单独写出来的
####################################
# 首先判断角色的unique的数量>100

holding = {}  # 将得出的数据存储

for j in separate_dialogue:
    file = open('32009682_' + j.lower() + '.txt', 'r')
    # file = open('32009682_' + 'monica' + '.txt', 'r')
    data = file.read()

    # 去掉所有的换行符
    new_data = data.replace("\n", "")

    character_dialogue = new_data.split(' ')

    # 找出一个角色里面不重复的单词
    unique_word = set(character_dialogue)

    if len(unique_word) > 100:
        ############################
        # 进行行频率计算

        from collections import Counter

        # 根据要求，不区分大小写，所以统一换成小写
        lower_data = data.lower()

        new_list = lower_data.split("\n")

        # 将每一行去重后的元素一起计算，则得到行频率
        separate_word = []
        # 因为写进文件的时候最后一行是\n，所以专门不去读取它
        for i in new_list[:-1]:
            # 将每一行末尾的空格删去
            list_dialogue = i.strip().split(" ")
            # 将每一行的重复元素去掉
            new_set = set(list_dialogue)
            separate_word += new_set

        word_counter = Counter(separate_word)  # 取出每个单词出现的个数

        highest_frequencies = word_counter.most_common(5)  # 取出频率最高的前5个
        # print(highest_frequencies)

        ################################
        # 存入到pandas

        import pandas as pd

        df = pd.DataFrame(highest_frequencies, columns=['word', 'freq'])

        # 将role的这一列插到最前面
        df.insert(0, 'role', j.lower())

        holding[j] = df

final = pd.concat(list(holding.values()), ignore_index=True)
print(final)
final.to_csv('32009682_data.csv')

#####################
# 以下是task4的内容

import matplotlib.pyplot as plt
final.plot(x='word',kind='bar')
plt.show()