test_list = ['126','371','118']

with open('test2.txt','w') as f:
    f.write('\n'.join(test_list))

def checkArmstrong(filename):
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            digit_num = int(line)
            total_num = 0
            for num in line:
                total_num += int(num) ** 3
            if total_num == digit_num:
                print(True)
            else:
                print(False)


checkArmstrong('test2.txt')
